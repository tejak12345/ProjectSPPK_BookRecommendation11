from setuptools import setup  # Perbaiki impor hanya mengambil `setup`
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,  # Nama paket
    version="0.0.1",  # Versi paket
    author=AUTHOR_USER_NAME,  # Nama penulis
    description="Books Recommender System using Machine Learning",  # Deskripsi singkat
    long_description=long_description,  # Deskripsi panjang dari README.md
    long_description_content_type="text/markdown",  # Format deskripsi panjang
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL repositori
    author_email="entbappy73@gmail.com",  # Email penulis
    packages=[SRC_REPO],  # Paket yang disertakan
    python_requires=">=3.7",  # Versi Python minimum
    install_requires=LIST_OF_REQUIREMENTS  # Dependensi yang diperlukan
)
