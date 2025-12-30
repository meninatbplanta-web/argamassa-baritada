import os
from bs4 import BeautifulSoup
import re

def otimizar_sitemap():
    """Otimiza o sitemap.xml com prioridades corretas"""
    sitemap_path = '/home/ubuntu/argamassa-baritada/sitemap.xml'
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'xml')
        
        # Ajustar prioridades baseado na importância das páginas
        urls = soup.find_all('url')
        for url in urls:
            loc = url.find('loc')
            if loc:
                url_text = loc.text
                priority = url.find('priority')
                
                # Página principal
                if url_text.endswith('/') or 'index.html' in url_text:
                    if priority:
                        priority.string = '1.0'
                # Páginas principais de conteúdo
                elif any(x in url_text for x in ['o-que-e', 'como-aplicar', 'preco', 'rendimento']):
                    if priority:
                        priority.string = '0.9'
                # Páginas de cidades
                elif 'argamassa-baritada-' in url_text:
                    if priority:
                        priority.string = '0.7'
                # Outras páginas
                else:
                    if priority:
                        priority.string = '0.8'
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("✓ Sitemap otimizado")
        return True
    except Exception as e:
        print(f"❌ Erro ao otimizar sitemap: {e}")
        return False

def otimizar_robots_txt():
    """Otimiza o robots.txt"""
    robots_path = '/home/ubuntu/argamassa-baritada/robots.txt'
    try:
        robots_content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://www.marketsite.com.br/sitemap.xml

# Páginas prioritárias para crawling
Allow: /index.html
Allow: /o-que-e-argamassa-baritada.html
Allow: /como-aplicar-argamassa-baritada.html
Allow: /preco-argamassa-baritada.html
Allow: /rendimento-argamassa-baritada.html
Allow: /blindagem-radiologica.html
Allow: /calculadora-argamassa.html
"""
        
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots_content)
        
        print("✓ Robots.txt otimizado")
        return True
    except Exception as e:
        print(f"❌ Erro ao otimizar robots.txt: {e}")
        return False

def adicionar_links_internos_estrategicos(filepath):
    """Adiciona links internos estratégicos nas páginas"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # Encontrar o conteúdo principal
        article = soup.find('article') or soup.find('main')
        if not article:
            return False
        
        # Adicionar links contextuais no texto
        paragraphs = article.find_all('p')
        for p in paragraphs:
            text = p.get_text()
            
            # Link para calculadora quando mencionar "consumo" ou "quantidade"
            if ('consumo' in text.lower() or 'quantidade' in text.lower()) and 'calculadora' not in text.lower():
                if not p.find('a', href='calculadora-argamassa.html'):
                    # Adicionar link contextual
                    new_text = text.replace('consumo', '<a href="calculadora-argamassa.html">consumo</a>', 1)
                    p.clear()
                    p.append(BeautifulSoup(new_text, 'html.parser'))
            
            # Link para página de preço quando mencionar "custo" ou "preço"
            if ('preço' in text.lower() or 'custo' in text.lower()) and 'preco-argamassa' not in str(p):
                if not p.find('a', href='preco-argamassa-baritada.html'):
                    new_text = text.replace('preço', '<a href="preco-argamassa-baritada.html" style="color:var(--primary); font-weight:600;">preço</a>', 1)
                    p.clear()
                    p.append(BeautifulSoup(new_text, 'html.parser'))
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        return True
    except Exception as e:
        print(f"❌ Erro ao adicionar links internos em {filepath}: {e}")
        return False

def adicionar_faq_schema_em_todas_paginas():
    """Adiciona FAQ schema em páginas relevantes"""
    paginas_com_faq = [
        'preco-argamassa-baritada.html',
        'como-aplicar-argamassa-baritada.html',
        'rendimento-argamassa-baritada.html'
    ]
    
    for pagina in paginas_com_faq:
        filepath = f'/home/ubuntu/argamassa-baritada/{pagina}'
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                # Verificar se já tem FAQ schema
                existing_faq = soup.find('script', type='application/ld+json', string=lambda t: t and 'FAQPage' in t)
                if not existing_faq:
                    # Adicionar FAQ schema genérico
                    faq_schema = soup.new_tag('script', type='application/ld+json')
                    faq_schema.string = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Quanto custa a argamassa baritada?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "O preço da argamassa baritada varia entre R$ 45 e R$ 85 por saco de 25kg, dependendo da densidade, laudo e logística de entrega."
    }
  }]
}'''
                    head = soup.find('head')
                    if head:
                        head.append(faq_schema)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    print(f"✓ FAQ schema adicionado em {pagina}")
            except Exception as e:
                print(f"❌ Erro ao processar {pagina}: {e}")

# Executar otimizações
print("=== Iniciando Melhorias Técnicas e Estruturais ===\n")

otimizar_sitemap()
otimizar_robots_txt()

print("\n=== Adicionando FAQ Schema ===")
adicionar_faq_schema_em_todas_paginas()

print("\n✅ Melhorias técnicas e estruturais aplicadas com sucesso!")
