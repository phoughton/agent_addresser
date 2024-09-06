
## Mapping of Mnemonic to description and datatype etc in ISO20022 addresses

| Description          | Mnemonic    | Occurences | Data Type      | Definition                                                                                                                  |
| -------------------  | ----------- | ---------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Department           | Dept        | [0..1]     | text{1,70}     | Identification of a division of a large organisation or building.                                                           |
| Sub Department       | SubDept     | [0..1]     | text{1,70}     | Identification of a sub-division of a large organisation or building.                                                       |
| Street Name          | StrtNm      | [0..1]     | text{1,70}     | Name of a street or thoroughfare.                                                                                           |
| Building Number      | BldgNb      | [0..1]     | text{1,16}     | Number that identifies the position of a building on a street.                                                              |
| Building Name        | BldgNm      | [0..1]     | text{1,35}     | Name of the building or house.                                                                                              |
| Floor                | Flr         | [0..1]     | text{1,70}     | Floor or storey within a building.                                                                                          |
| Post Box             | PstBx       | [0..1]     | text{1,16}     | Numbered box in a post office, assigned to a person or organisation, where letters are kept until called for.               |
| Room                 | Room        | [0..1]     | text{1,70}     | Building room number.                                                                                                       |
| Post Code            | PstCd       | [0..1]     | text{1,16}     | Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail. |
| Town Name            | TwnNm       | [0..1]     | text{1,35}     | Name of a built-up area, with defined boundaries, and a local government.                                                   |
| Town Location Name   | TwnLctnNm   | [0..1]     | text{1,35}     | Specific location name within the town.                                                                                     |
| District Name        | DstrctNm    | [0..1]     | text{1,35}     | Identifies a subdivision within a country sub-division.                                                                     |
| Country Sub-Division | CtrySubDvsn | [0..1]     | text{1,35}     | Identifies a subdivision of a country such as state, region, county.                                                        |
| Country              | Ctry        | [0..1]     | text[A-Z]{2,2} | Nation with its own government.                                                                                             |

Fully structured is preferred, using the mnemonics above. 
