# Converting free text into structured data

Large Language Models are surprisingly good ad parsing addresses, but they need help to do it.

This code contains a a collection of examples as prompts collated into a simnple tool that can parse your text into a structured address.

Its built around the ISO20022 address used in PACS008.001.08 (for CBPR+). Why? Well thats the initial version thats planned to roll out late in 2025.

(I focus on the fully structured address for now, as opposed to the Hybrid address, as thats the interesting technical challenge.)

## Getting Started...


Set up an environment variable called "OPENAI_API_KEY", with the value of your OPENAI API key 

(You can set one up here: https://platform.openai.com/api-keys )

### For JSON:
```bash
python addr_raw_to_iso_structured.py 
```

Should return: 
```json
{
    "Nm": "Fake Moon Landings Inc.",
    "PstlAdr": {
        "StrtNm": "Fordpark Road",
        "BldgNm": "Central Business Centre",
        "Room": "Suite 999",
        "PstCd": "L40 2OP",
        "TwnNm": "Newcastle upon Tyne",
        "Ctry": "GB"
    }
} 
```


### For XML:
```bash
python addr_raw_to_iso_structured.py --format xml
```

Should return: 
```json
<?xml version="1.0" ?>
<Cdtr>
        <Nm>Fake Moon Landings Inc.</Nm>
        <PstlAdr>
                <StrtNm>Fordpark Road</StrtNm>
                <BldgNm>Central Business Centre</BldgNm>
                <Room>Suite 999</Room>
                <PstCd>L40 2OP</PstCd>
                <TwnNm>Newcastle upon Tyne</TwnNm>
                <Ctry>GB</Ctry>
        </PstlAdr>
</Cdtr>
```