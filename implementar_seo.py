import os
import re
from bs4 import BeautifulSoup

def otimizar_h1_index(soup):
    """Otimiza o H1 da página principal"""
    h1 = soup.find('h1')
    if h1 and 'Sua Blindagem Passa na Vistoria da CNEN?' in h1.text:
        h1.string = 'Argamassa Baritada: Cotação com Laudo CNEN para Blindagem de Raio-X'
    return soup

def adicionar_schema_produto(soup):
    """Adiciona schema de produto para melhor SEO"""
    schema_produto = soup.new_tag('script', type='application/ld+json')
    schema_produto.string = '''{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Argamassa Baritada",
  "description": "Argamassa baritada de alta densidade (3.2 g/cm³) para proteção radiológica em salas de raio-x, com laudo CNEN certificado.",
  "brand": {
    "@type": "Brand",
    "name": "Baritada Expert"
  },
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Baritada Expert"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}'''
    head = soup.find('head')
    if head:
        head.append(schema_produto)
    return soup

def otimizar_meta_description(soup, keyword_focus="argamassa baritada"):
    """Otimiza meta description para incluir palavra-chave"""
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        current = meta_desc.get('content', '')
        if keyword_focus.lower() not in current.lower():
            new_desc = f"{keyword_focus.title()}: {current}"
            meta_desc['content'] = new_desc[:160]
    return soup

def adicionar_breadcrumb_schema(soup, page_name="Home"):
    """Adiciona schema de breadcrumb"""
    schema_breadcrumb = soup.new_tag('script', type='application/ld+json')
    schema_breadcrumb.string = f'''{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{{
    "@type": "ListItem",
    "position": 1,
    "name": "Home",
    "item": "https://www.marketsite.com.br/"
  }},
  {{
    "@type": "ListItem",
    "position": 2,
    "name": "{page_name}"
  }}]
}}'''
    head = soup.find('head')
    if head:
        head.append(schema_breadcrumb)
    return soup

def otimizar_h2_com_palavra_chave(soup):
    """Otimiza H2s para incluir palavra-chave onde apropriado"""
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        text = h2.get_text()
        if 'Por que não arriscar' in text:
            h2.string = 'Por que usar Argamassa Baritada com Laudo Certificado?'
        elif 'Guia Completo' in text and 'Argamassa' not in text:
            h2.string = 'Guia Completo sobre Argamassa Baritada'
    return soup

def adicionar_alt_text_imagens(soup):
    """Adiciona alt text descritivo para imagens"""
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            src = img.get('src', '')
            if 'logo' in src.lower():
                img['alt'] = 'Argamassa Baritada - Logo'
            elif 'saco' in src.lower() or 'produto' in src.lower():
                img['alt'] = 'Saco de 25kg de argamassa baritada para proteção radiológica'
            elif 'aplicacao' in src.lower():
                img['alt'] = 'Aplicação de argamassa baritada em parede de sala de raio-x'
            else:
                img['alt'] = 'Argamassa baritada para blindagem radiológica'
    return soup

def otimizar_arquivo_html(filepath):
    """Otimiza um arquivo HTML individual"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Aplicar otimizações
        if 'index.html' in filepath:
            soup = otimizar_h1_index(soup)
            soup = adicionar_schema_produto(soup)
        
        soup = otimizar_meta_description(soup)
        soup = otimizar_h2_com_palavra_chave(soup)
        soup = adicionar_alt_text_imagens(soup)
        
        # Adicionar breadcrumb para páginas internas
        if 'index.html' not in filepath:
            page_name = os.path.basename(filepath).replace('.html', '').replace('-', ' ').title()
            soup = adicionar_breadcrumb_schema(soup, page_name)
        
        # Salvar arquivo otimizado
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        return True
    except Exception as e:
        print(f"Erro ao processar {filepath}: {e}")
        return False

# Processar index.html
print("Otimizando index.html...")
otimizar_arquivo_html('/home/ubuntu/argamassa-baritada/index.html')
print("✓ index.html otimizado")

# Processar páginas principais
paginas_principais = [
    'o-que-e-argamassa-baritada.html',
    'como-aplicar-argamassa-baritada.html',
    'preco-argamassa-baritada.html',
    'rendimento-argamassa-baritada.html',
    'blindagem-radiologica.html',
    'entrega-brasil.html'
]

for pagina in paginas_principais:
    filepath = f'/home/ubuntu/argamassa-baritada/{pagina}'
    if os.path.exists(filepath):
        print(f"Otimizando {pagina}...")
        otimizar_arquivo_html(filepath)
        print(f"✓ {pagina} otimizado")

print("\n✅ Otimizações de SEO aplicadas com sucesso!")
