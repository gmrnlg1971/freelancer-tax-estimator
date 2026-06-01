import json

states_data = {
    "AL": {"name": "Alabama", "type": "progressive", "std": 3000, "brackets": [{"limit": 500, "rate": 0.02}, {"limit": 3000, "rate": 0.04}, {"limit": float('inf'), "rate": 0.05}]},
    "AK": {"name": "Alaska", "type": "flat", "rate": 0},
    "AZ": {"name": "Arizona", "type": "flat", "rate": 0.025},
    "AR": {"name": "Arkansas", "type": "progressive", "std": 2340, "brackets": [{"limit": 4400, "rate": 0.02}, {"limit": 8800, "rate": 0.04}, {"limit": float('inf'), "rate": 0.044}]},
    "CA": {"name": "California", "type": "progressive", "std": 5363, "brackets": [{"limit": 10412, "rate": 0.01}, {"limit": 24684, "rate": 0.02}, {"limit": 38959, "rate": 0.04}, {"limit": 54081, "rate": 0.06}, {"limit": 68350, "rate": 0.08}, {"limit": 349137, "rate": 0.093}, {"limit": 418961, "rate": 0.103}, {"limit": 698271, "rate": 0.113}, {"limit": float('inf'), "rate": 0.123}]},
    "CO": {"name": "Colorado", "type": "flat", "rate": 0.044},
    "CT": {"name": "Connecticut", "type": "progressive", "std": 0, "brackets": [{"limit": 10000, "rate": 0.03}, {"limit": 50000, "rate": 0.05}, {"limit": 100000, "rate": 0.055}, {"limit": 250000, "rate": 0.06}, {"limit": 500000, "rate": 0.065}, {"limit": float('inf'), "rate": 0.0699}]},
    "DE": {"name": "Delaware", "type": "progressive", "std": 3250, "brackets": [{"limit": 2000, "rate": 0}, {"limit": 5000, "rate": 0.022}, {"limit": 10000, "rate": 0.039}, {"limit": 20000, "rate": 0.048}, {"limit": 25000, "rate": 0.052}, {"limit": 60000, "rate": 0.0555}, {"limit": float('inf'), "rate": 0.066}]},
    "FL": {"name": "Florida", "type": "flat", "rate": 0},
    "GA": {"name": "Georgia", "type": "flat", "rate": 0.0549},
    "HI": {"name": "Hawaii", "type": "progressive", "std": 2200, "brackets": [{"limit": 2400, "rate": 0.014}, {"limit": 4800, "rate": 0.032}, {"limit": 9600, "rate": 0.055}, {"limit": 14400, "rate": 0.064}, {"limit": 19200, "rate": 0.068}, {"limit": 24000, "rate": 0.072}, {"limit": 36000, "rate": 0.076}, {"limit": 48000, "rate": 0.079}, {"limit": 150000, "rate": 0.0825}, {"limit": 175000, "rate": 0.09}, {"limit": 200000, "rate": 0.10}, {"limit": float('inf'), "rate": 0.11}]},
    "ID": {"name": "Idaho", "type": "flat", "rate": 0.058},
    "IL": {"name": "Illinois", "type": "flat", "rate": 0.0495},
    "IN": {"name": "Indiana", "type": "flat", "rate": 0.0305},
    "IA": {"name": "Iowa", "type": "flat", "rate": 0.057},
    "KS": {"name": "Kansas", "type": "progressive", "std": 3500, "brackets": [{"limit": 15000, "rate": 0.031}, {"limit": 30000, "rate": 0.0525}, {"limit": float('inf'), "rate": 0.057}]},
    "KY": {"name": "Kentucky", "type": "flat", "rate": 0.04},
    "LA": {"name": "Louisiana", "type": "progressive", "std": 4500, "brackets": [{"limit": 12500, "rate": 0.0185}, {"limit": 50000, "rate": 0.035}, {"limit": float('inf'), "rate": 0.0425}]},
    "ME": {"name": "Maine", "type": "progressive", "std": 14600, "brackets": [{"limit": 24500, "rate": 0.058}, {"limit": 58050, "rate": 0.0715}, {"limit": float('inf'), "rate": 0.0715}]},
    "MD": {"name": "Maryland", "type": "progressive", "std": 2550, "brackets": [{"limit": 1000, "rate": 0.02}, {"limit": 2000, "rate": 0.03}, {"limit": 3000, "rate": 0.04}, {"limit": 100000, "rate": 0.0475}, {"limit": 125000, "rate": 0.05}, {"limit": 150000, "rate": 0.0525}, {"limit": 250000, "rate": 0.055}, {"limit": float('inf'), "rate": 0.0575}]},
    "MA": {"name": "Massachusetts", "type": "flat", "rate": 0.05},
    "MI": {"name": "Michigan", "type": "flat", "rate": 0.0425},
    "MN": {"name": "Minnesota", "type": "progressive", "std": 13825, "brackets": [{"limit": 30070, "rate": 0.0535}, {"limit": 98760, "rate": 0.068}, {"limit": 183340, "rate": 0.0785}, {"limit": float('inf'), "rate": 0.0985}]},
    "MS": {"name": "Mississippi", "type": "flat", "rate": 0.047},
    "MO": {"name": "Missouri", "type": "progressive", "std": 14600, "brackets": [{"limit": 1208, "rate": 0}, {"limit": 2416, "rate": 0.02}, {"limit": 3624, "rate": 0.025}, {"limit": 4832, "rate": 0.03}, {"limit": 6040, "rate": 0.035}, {"limit": 7248, "rate": 0.04}, {"limit": 8456, "rate": 0.045}, {"limit": float('inf'), "rate": 0.0495}]},
    "MT": {"name": "Montana", "type": "progressive", "std": 5540, "brackets": [{"limit": 3600, "rate": 0.047}, {"limit": float('inf'), "rate": 0.059}]},
    "NE": {"name": "Nebraska", "type": "progressive", "std": 7900, "brackets": [{"limit": 3700, "rate": 0.0246}, {"limit": 22170, "rate": 0.0351}, {"limit": 35730, "rate": 0.0501}, {"limit": float('inf'), "rate": 0.0584}]},
    "NV": {"name": "Nevada", "type": "flat", "rate": 0},
    "NH": {"name": "New Hampshire", "type": "flat", "rate": 0},
    "NJ": {"name": "New Jersey", "type": "progressive", "std": 1000, "brackets": [{"limit": 20000, "rate": 0.014}, {"limit": 35000, "rate": 0.0175}, {"limit": 40000, "rate": 0.035}, {"limit": 75000, "rate": 0.0552}, {"limit": 500000, "rate": 0.0637}, {"limit": 1000000, "rate": 0.0897}, {"limit": float('inf'), "rate": 0.1075}]},
    "NM": {"name": "New Mexico", "type": "progressive", "std": 14600, "brackets": [{"limit": 5500, "rate": 0.017}, {"limit": 11000, "rate": 0.032}, {"limit": 16000, "rate": 0.047}, {"limit": 210000, "rate": 0.049}, {"limit": float('inf'), "rate": 0.059}]},
    "NY": {"name": "New York", "type": "progressive", "std": 8000, "brackets": [{"limit": 8500, "rate": 0.04}, {"limit": 11700, "rate": 0.045}, {"limit": 13900, "rate": 0.0525}, {"limit": 80650, "rate": 0.055}, {"limit": 215400, "rate": 0.06}, {"limit": 1077550, "rate": 0.0685}, {"limit": 5000000, "rate": 0.0965}, {"limit": 25000000, "rate": 0.103}, {"limit": float('inf'), "rate": 0.109}]},
    "NC": {"name": "North Carolina", "type": "flat", "rate": 0.045},
    "ND": {"name": "North Dakota", "type": "progressive", "std": 14600, "brackets": [{"limit": 44725, "rate": 0.011}, {"limit": 108150, "rate": 0.0204}, {"limit": 225975, "rate": 0.0227}, {"limit": float('inf'), "rate": 0.025}]},
    "OH": {"name": "Ohio", "type": "progressive", "std": 0, "brackets": [{"limit": 26050, "rate": 0}, {"limit": 100000, "rate": 0.0275}, {"limit": float('inf'), "rate": 0.035}]},
    "OK": {"name": "Oklahoma", "type": "progressive", "std": 6350, "brackets": [{"limit": 1000, "rate": 0.0025}, {"limit": 2500, "rate": 0.0075}, {"limit": 3750, "rate": 0.0175}, {"limit": 4900, "rate": 0.0275}, {"limit": 7200, "rate": 0.0375}, {"limit": float('inf'), "rate": 0.0475}]},
    "OR": {"name": "Oregon", "type": "progressive", "std": 2605, "brackets": [{"limit": 4050, "rate": 0.0475}, {"limit": 10200, "rate": 0.0675}, {"limit": 125000, "rate": 0.0875}, {"limit": float('inf'), "rate": 0.099}]},
    "PA": {"name": "Pennsylvania", "type": "flat", "rate": 0.0307},
    "RI": {"name": "Rhode Island", "type": "progressive", "std": 10000, "brackets": [{"limit": 73450, "rate": 0.0375}, {"limit": 166950, "rate": 0.0475}, {"limit": float('inf'), "rate": 0.0599}]},
    "SC": {"name": "South Carolina", "type": "progressive", "std": 14600, "brackets": [{"limit": 3460, "rate": 0}, {"limit": 17330, "rate": 0.03}, {"limit": float('inf'), "rate": 0.064}]},
    "SD": {"name": "South Dakota", "type": "flat", "rate": 0},
    "TN": {"name": "Tennessee", "type": "flat", "rate": 0},
    "TX": {"name": "Texas", "type": "flat", "rate": 0},
    "UT": {"name": "Utah", "type": "flat", "rate": 0.0465},
    "VT": {"name": "Vermont", "type": "progressive", "std": 7450, "brackets": [{"limit": 43950, "rate": 0.0335}, {"limit": 106350, "rate": 0.066}, {"limit": 218200, "rate": 0.076}, {"limit": float('inf'), "rate": 0.0875}]},
    "VA": {"name": "Virginia", "type": "progressive", "std": 8000, "brackets": [{"limit": 3000, "rate": 0.02}, {"limit": 5000, "rate": 0.03}, {"limit": 17000, "rate": 0.05}, {"limit": float('inf'), "rate": 0.0575}]},
    "WA": {"name": "Washington", "type": "flat", "rate": 0},
    "WV": {"name": "West Virginia", "type": "progressive", "std": 0, "brackets": [{"limit": 10000, "rate": 0.0236}, {"limit": 25000, "rate": 0.0315}, {"limit": 40000, "rate": 0.0354}, {"limit": 60000, "rate": 0.0472}, {"limit": float('inf'), "rate": 0.0512}]},
    "WI": {"name": "Wisconsin", "type": "progressive", "std": 12560, "brackets": [{"limit": 13810, "rate": 0.035}, {"limit": 27630, "rate": 0.044}, {"limit": 304170, "rate": 0.053}, {"limit": float('inf'), "rate": 0.0765}]},
    "WY": {"name": "Wyoming", "type": "flat", "rate": 0}
}

options_html = ""
for code, data in states_data.items():
    options_html += f'<option value="{code}">{data["name"]}</option>\n'

json_data = "{\n"
for code, data in states_data.items():
    if data["type"] == "flat":
        json_data += f'  "{code}": {{ type: "flat", rate: {data["rate"]} }},\n'
    else:
        brackets_str = "[\n"
        for b in data["brackets"]:
            limit_str = "Infinity" if b["limit"] == float('inf') else b["limit"]
            brackets_str += f'      {{ limit: {limit_str}, rate: {b["rate"]} }},\n'
        brackets_str += "    ]"
        json_data += f'  "{code}": {{ type: "progressive", std: {data["std"]}, brackets: {brackets_str} }},\n'
json_data += "}"

print("=== HTML OPTIONS ===")
print(options_html)
print("=== JSON DATA ===")
print(json_data)
