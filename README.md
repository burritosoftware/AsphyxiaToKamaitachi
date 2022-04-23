# AsphyxiaToKamaitachi

An importer for Asphyxia servers to transfer scores to Kamaitachi.

## Requirements
- Python 3.10+

## Instructions

1. Place an `sdvx@asphyxia.db` and a `music_db.xml` file next to `create.py`.
> The music_db.xml file must NOT have multi-byte encodings, or the importer will error. An easy way around this is to create a new XML file, then manually copy and paste the contents to the new one.

2. Install requirements. (You only need to do this once.)
```py
pip install -r requirements.txt
```

3. Launch the importer, then follow the instructions.
```
py create.py
```