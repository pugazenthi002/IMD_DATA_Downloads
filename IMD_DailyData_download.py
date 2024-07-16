import pandas as pd
url1 = 'http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWSAGRO&b=TAMIL_NADU&c=COIMBATORE&d=UPASI_TEA_RESEARCH_FOUNDATION&e=2024-07-04&f=2024-07-11&g=ALL_HOUR&h=ALL_MINUTE'
dff = pd.read_html(url1)
df = dff[0]
df.to_csv('rmcaws.csv')
