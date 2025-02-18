import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Step 1: Generate Dummy Data for 70+ Portfolio Companies
np.random.seed(42)

companies = pd.DataFrame({
    'company_id': np.arange(1, 71),
    'company_name': ['Company_' + str(i) for i in range(1, 71)],
    'sector': np.random.choice(['Finance', 'Healthcare', 'Energy', 'Technology', 'Agriculture'], 70),
    'region': np.random.choice(['North America', 'Europe', 'Asia', 'South America', 'Africa'], 70),
    'access_to_finance_score': np.random.uniform(0, 100, 70),
    'essential_services_score': np.random.uniform(0, 100, 70),
    'job_creation_score': np.random.uniform(0, 100, 70),
    'ESG_deficiencies_score': np.random.uniform(0, 100, 70),
    'climate_policy_score': np.random.uniform(0, 100, 70),
    'scope1_emissions': np.random.randint(100, 1000, 70),
    'scope2_emissions': np.random.randint(200, 1500, 70),
    'scope3_emissions': np.random.randint(300, 2000, 70),
    'gender_pay_gap': np.random.uniform(5, 25, 70),
    'biodiversity_impact': np.random.uniform(1, 10, 70),
    'local_community_impact': np.random.uniform(0, 100, 70)
})

# 🔹 Step 2: Portfolio Evaluation Metrics
impact_metrics = companies[['access_to_finance_score', 'essential_services_score', 'job_creation_score']].mean()
print("📊 Portfolio Impact Metrics (Averages):\n", impact_metrics)

# 🔹 Step 3: ESG Monitoring
esg_metrics = companies[['ESG_deficiencies_score', 'climate_policy_score', 'gender_pay_gap', 'biodiversity_impact']].mean()
print("♻️ ESG Metrics Overview (Averages):\n", esg_metrics)

# 🔹 Step 4: Emissions Tracking (Scope 1, 2, 3)
emissions_summary = companies[['scope1_emissions', 'scope2_emissions', 'scope3_emissions']].sum()
print("🌍 Total Emissions (Scope 1, 2, 3):\n", emissions_summary)

# 🔹 Step 5: Supply Chain Evaluation - Scope 3 Emissions
top_emitters = companies.nlargest(5, 'scope3_emissions')
print("🚨 Top 5 Companies by Scope 3 Emissions:\n", top_emitters[['company_name', 'scope3_emissions']])

# 🔹 Step 6: Visualizations
plt.figure(figsize=(12, 6))
sns.barplot(x='region', y='scope3_emissions', data=companies, palette='coolwarm')
plt.title('Scope 3 Emissions by Region')
plt.show()

# 🔹 Step 7: ESG Deficiencies Monitoring
plt.figure(figsize=(14, 7))
sns.boxplot(x='sector', y='ESG_deficiencies_score', data=companies)
plt.title('ESG Deficiencies by Sector')
plt.show()

# 🔹 Step 8: Save Portfolio Data
companies.to_csv('Portfolio_Management_ESG.csv', index=False)
print("📄 Portfolio data saved as 'Portfolio_Management_ESG.csv'")
