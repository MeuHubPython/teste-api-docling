import os
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException  # type: ignore
from docling.document_converter import DocumentConverter

app = FastAPI()
converter = DocumentConverter()


@app.post("/convert")
async def convert_pdf_to_markdown(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um PDF.")

    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            contents = await file.read()
            tmp_file.write(contents)
            tmp_path = tmp_file.name

        result = converter.convert(tmp_path)
        if not getattr(result, "success", True):
            raise HTTPException(status_code=500, detail="Erro ao processar o PDF.")

        markdown = result.document.export_to_markdown()
        return {"markdown": markdown}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
