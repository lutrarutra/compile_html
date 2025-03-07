import os
import base64
from bs4 import BeautifulSoup
from typing import Optional


def encode_file(filepath: str, mime_type: str) -> str:
    """Encodes a file as a Base64 string."""
    with open(filepath, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def inline_assets(html_path: str, folder: str) -> str:
    """Embeds CSS, JS, and images into a single HTML file."""
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    # Inline CSS
    for link in soup.find_all("link", rel="stylesheet"):
        css_file: Optional[str] = link.get("href")
        if css_file:
            css_path: str = os.path.join(folder, css_file)
            if os.path.exists(css_path):
                with open(css_path, "r", encoding="utf-8") as f:
                    style_tag = soup.new_tag("style")
                    style_tag.string = f.read()
                    link.replace_with(style_tag)
    
    # Inline JS
    for script in soup.find_all("script", src=True):
        js_file: Optional[str] = script.get("src")
        if js_file:
            js_path: str = os.path.join(folder, js_file)
            if os.path.exists(js_path):
                with open(js_path, "r", encoding="utf-8") as f:
                    script_tag = soup.new_tag("script")
                    script_tag.string = f.read()
                    script.replace_with(script_tag)
    
    # Inline images
    for img in soup.find_all("img", src=True):
        img_file: str = img["src"]
        img_path: str = os.path.join(folder, img_file)
        if os.path.exists(img_path):
            ext: str = os.path.splitext(img_file)[1][1:]  # Get file extension
            mime_type: str = f"image/{ext}" if ext else "image/png"
            img["src"] = encode_file(img_path, mime_type)
    
    return str(soup)


def make_standalone_html(source_folder: str, output_file: str, main_html: str = "index.html") -> None:
    """Creates a standalone HTML file from a folder of assets."""
    main_html_path: str = os.path.join(source_folder, main_html)
    if not os.path.exists(main_html_path):
        raise FileNotFoundError(f"ERROR: Main HTML file not found: {main_html_path}")
    
    final_html: str = inline_assets(main_html_path, source_folder)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print(f"Standalone HTML saved to {output_file}")