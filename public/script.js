async function analyzeEmail() {
  const email = document.getElementById("emailInput").value;

  document.getElementById("loading").innerHTML = "Analyzing...";

  try {
    // Local FastAPI backend
    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        email: email,
      }),
    });

    // Handle backend/server errors
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

    document.getElementById("loading").innerHTML = "";

    // Main Result Display
    document.getElementById("result").innerHTML = `

            <h2>
                ${data.final_result.prediction}
            </h2>

            <p>
                Final Score:
                ${data.final_result.final_score}
            </p>

            <h3>
                Reasons
            </h3>

            <ul>
                ${data.final_result.reasons
                  .map((reason) => `<li>${reason}</li>`)
                  .join("")}
            </ul>

            ${
              data.domain_result && data.domain_result.is_suspicious
                ? `
                    <h3>
                        Suggested Legitimate Website
                    </h3>

                    <p>
                        <a href="https://${data.domain_result.suggested_domain}"
                           target="_blank">

                           ${data.domain_result.suggested_domain}

                        </a>
                    </p>
                    `
                : ""
            }

        `;

    // SHAP Explainability Output (Optional)
    if (data.shap_html && document.getElementById("shap")) {
      document.getElementById("shap").innerHTML = data.shap_html;
    }
  } catch (error) {
    console.error("Frontend Error:", error);

    document.getElementById("loading").innerHTML = "";

    document.getElementById("result").innerHTML = `

            <h2>
                Error connecting to backend
            </h2>

            <p>
                Make sure FastAPI is running on:
                http://127.0.0.1:8000
            </p>

        `;

    // Clear SHAP safely
    if (document.getElementById("shap")) {
      document.getElementById("shap").innerHTML = "";
    }
  }
}
