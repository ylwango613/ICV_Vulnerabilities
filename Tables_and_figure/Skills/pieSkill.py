import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"]=(12,5)
plt.rcParams["font.family"]="Times New Roman"
plt.rcParams["font.size"]=20
# plt.rcParams["font.weight"]="bold"

Riskbar = ["Penetration testing", "Port scanning", "Traffic analysis", "Reverse engineering", "Signal interception"]
counts = [356,97,80,75,41]
# 推荐的颜色
colors = ["#4874CB", "#EE822F", "#F2BA02", "#75BD42", "#30C0B4"]
bar = plt.pie(counts, labels=Riskbar, autopct=lambda pct: f"{int(pct/100*sum(counts))}, {pct:.1f}%", pctdistance=0.75,textprops={'fontsize': 14}, colors=colors)
plt.savefig("pieSkill.pdf", bbox_inches="tight")
plt.show()