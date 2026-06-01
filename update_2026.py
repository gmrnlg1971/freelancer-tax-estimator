import re

with open('src/pages/index.astro', 'r') as f:
    content = f.read()

# Replace simple strings
content = content.replace('based on 2024 US tax brackets.', 'based on 2026 US tax brackets.')
content = content.replace('Estimated Breakdown (2024)', 'Estimated Breakdown (2026)')
content = content.replace('simplified estimate for 2024 using', 'simplified estimate for 2026 using')
content = content.replace('($168,600 for 2024)', '($175,000 for 2026)')
content = content.replace('standardDeduction2024', 'standardDeduction2026')
content = content.replace('brackets2024', 'brackets2026')
content = content.replace('// 2024 Tax Brackets', '// 2026 Tax Brackets')

# Replace brackets object using regex
old_brackets = re.compile(r'const brackets2026 = \{.*?^\t\};', re.MULTILINE | re.DOTALL)
new_brackets = """const brackets2026 = {
		single: [
			{ limit: 12400, rate: 0.10 },
			{ limit: 50400, rate: 0.12 },
			{ limit: 105700, rate: 0.22 },
			{ limit: 201775, rate: 0.24 },
			{ limit: 256225, rate: 0.32 },
			{ limit: 640600, rate: 0.35 },
			{ limit: Infinity, rate: 0.37 }
		],
		married: [
			{ limit: 24800, rate: 0.10 },
			{ limit: 100800, rate: 0.12 },
			{ limit: 211400, rate: 0.22 },
			{ limit: 403550, rate: 0.24 },
			{ limit: 512450, rate: 0.32 },
			{ limit: 768700, rate: 0.35 },
			{ limit: Infinity, rate: 0.37 }
		]
	};"""
content = old_brackets.sub(new_brackets, content)

# Replace standard deductions using regex
old_deductions = re.compile(r'const standardDeduction2026 = \{.*?^\t\};', re.MULTILINE | re.DOTALL)
new_deductions = """const standardDeduction2026 = {
		single: 16100,
		married: 32200
	};"""
content = old_deductions.sub(new_deductions, content)

with open('src/pages/index.astro', 'w') as f:
    f.write(content)

print("Updated index.astro to 2026 compliance")
