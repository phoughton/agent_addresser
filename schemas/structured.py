from pydantic import BaseModel, Field
from typing import Optional


class PostalAddress(BaseModel):
    Dept: Optional[str] = Field(None, description="Identification of a division of a large organisation or building.")
    SubDept: Optional[str] = Field(None, description="Identification of a sub-division of a large organisation or building.")
    StrtNm: Optional[str] = Field(None, description="Name of a street or thoroughfare.")
    BldgNb: Optional[str] = Field(None, description="Number that identifies the position of a building on a street.")
    BldgNm: Optional[str] = Field(None, description="Name of the building or house.")
    Flr: Optional[str] = Field(None, description="Floor or storey within a building.")
    PstBx: Optional[str] = Field(None, description="Numbered box in a post office assigned to a person or organisation.")
    Room: Optional[str] = Field(None, description="Building room number.")
    PstCd: Optional[str] = Field(None, description="Identifier added to a postal address to assist the sorting of mail.")
    TwnNm: Optional[str] = Field(None, description="Name of a built-up area with defined boundaries and a local government.")
    TwnLctnNm: Optional[str] = Field(None, description="Specific location name within the town.")
    DstrctNm: Optional[str] = Field(None, description="Identifies a subdivision within a country sub-division.")
    CtrySubDvsn: Optional[str] = Field(None, description="Identifies a subdivision of a country such as state, region, or county.")
    Ctry: Optional[str] = Field(None, description="Nation with its own government, represented as a 2-letter code.")


class Address(BaseModel):
    Nm: str = Field(..., description="Name of the organization.")
    PstlAdr: PostalAddress = Field(..., description="Postal address details.")
