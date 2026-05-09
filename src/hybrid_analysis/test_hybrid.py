from hybrid_score import hybrid_analysis

bert_score = 0.92
url_score = 0.7
domain_result = {"is_suspicious": True}
behavior_score = 0.6

result = hybrid_analysis(
    bert_score,
    url_score,
    domain_result,
    behavior_score
)

print("Final Result:")
print(result)