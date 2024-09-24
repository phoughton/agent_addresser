# Converting free text addresses into structured data

Large Language Models are surprisingly good at parsing addresses, but they need help to do it.

This code contains a collection of examples as prompts collated into a simple tool that can parse your text into a structured address.

Its built around the ISO20022 address used in PACS008.001.08 (for CBPR+). Why? Well thats the initial version thats planned to roll out late in 2025 - and it specifies a more detailed - field by field (preferred) format for addresses.

(I focus on the fully structured address for now, as opposed to the not-preferred Hybrid address, as thats the interesting technical challenge.)

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
```xml
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

### Specify a different example address:

You can specify another address by just pointing to the file...
```bash
python addr_raw_to_iso_structured.py --file test_examples/gucci_uk_addr_companies_house.txt
```

The output:
```json
{
    "Nm": "GUCCI LIMITED",
    "PstlAdr": {
        "StrtNm": "Perrymount Road",
        "BldgNb": "35",
        "BldgNm": "Oakfield House",
        "Flr": "5",
        "Room": "Rear Suite",
        "PstCd": "RH16 3BW",
        "TwnNm": "Haywards Heath",
        "CtrySubDvsn": "West Sussex",
        "Ctry": "GB"
    }
}
```
