"""
Hook para copiar slides HTML gerados para o site após build
"""
import shutil
import pathlib


def copy_slides(config, **kwargs):
    """
    Copia slides HTML e Markdown do diretório docs/slides/ para site/slides/
    após o build do MkDocs
    
    Args:
        config: Configuração do MkDocs
        **kwargs: Argumentos adicionais
    """
    site_dir = config['site_dir']
    slides_dest = pathlib.Path(site_dir) / 'slides'
    slides_dest.mkdir(exist_ok=True)
    
    # Diretório fonte dos slides
    slides_source = pathlib.Path('docs/slides')
    if not slides_source.exists():
        print("⚠ Pasta docs/slides/ não encontrada")
        return
    
    # Copiar todos os slides HTML e Markdown
    html_copied = 0
    md_copied = 0
    
    # Copiar HTML
    print("Copiando slides HTML...")
    for slide in slides_source.glob('slide-*.html'):
        dest_file = slides_dest / slide.name
        shutil.copy(slide.resolve(), dest_file.resolve())
        print(f"  → {slide.name}")
        html_copied += 1
    
    # Copiar Markdown
    print("Copiando slides Markdown...")
    for slide in slides_source.glob('slide-*.md'):  
        dest_file = slides_dest / slide.name
        shutil.copy(slide.resolve(), dest_file.resolve())
        print(f"  → {slide.name}")
        md_copied += 1
    
    if html_copied > 0:
        print(f"✓ {html_copied} slide(s) HTML copiados")
    if md_copied > 0:
        print(f"✓ {md_copied} slide(s) Markdown copiados")
    
    if html_copied == 0 and md_copied == 0:
        print("⚠ Nenhum slide encontrado em docs/slides/")


def on_post_build(config):
    """Hook chamado após o build do MkDocs"""
    copy_slides(config)
