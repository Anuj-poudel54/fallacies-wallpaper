from pydantic import BaseModel

class Fallacy(BaseModel):
    title: str
    desc: str
    ext_desc: str
    example: str


if __name__ == "__main__":
    f = Fallacy( title="sdfa", desc="dsflajsd", ext_desc="dfa;lsdjf", example="dafljsdf" )
    print(f.model_dump_json())