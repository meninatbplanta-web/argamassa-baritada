import os
from bs4 import BeautifulSoup
import json

def otimizar_title_tags():
    """Otimiza title tags para incluir palavra-chave e CTR"""
    otimizacoes = {
        'index.html': 'Argamassa Baritada: Cotação com Laudo CNEN | Entrega em Todo Brasil',
        'o-que-e-argamassa-baritada.html': 'O Que é Argamassa Baritada? Guia Completo 2025 | Composição e Uso',
        'como-aplicar-argamassa-baritada.html': 'Como Aplicar Argamassa Baritada: Passo a Passo Completo | Guia Prático',
        'preco-argamassa-baritada.html': 'Preço Argamassa Baritada 2025: Valores e Onde Comprar com Laudo',
        'rendimento-argamassa-baritada.html': 'Rendimento Argamassa Baritada: Calcule Quantos Sacos Você Precisa',
        'blindagem-radiologica.html': 'Blindagem Radiológica com Argamassa Baritada | Normas CNEN',
        'calculadora-argamassa.html': 'Calculadora de Argamassa Baritada: Calcule o Consumo por m²',
        'entrega-brasil.html': 'Entrega de Argamassa Baritada em Todo o Brasil | Frete Otimizado'
    }
    
    for arquivo, novo_title in otimizacoes.items():
        filepath = f'/home/ubuntu/argamassa-baritada/{arquivo}'
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                title_tag = soup.find('title')
                if title_tag:
                    title_tag.string = novo_title
                
                # Atualizar og:title também
                og_title = soup.find('meta', property='og:title')
                if og_title:
                    og_title['content'] = novo_title
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                print(f"✓ Title otimizado: {arquivo}")
            except Exception as e:
                print(f"❌ Erro em {arquivo}: {e}")

def adicionar_local_business_schema():
    """Adiciona LocalBusiness schema para SEO local"""
    filepath = '/home/ubuntu/argamassa-baritada/index.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # Verificar se já existe
        existing = soup.find('script', type='application/ld+json', string=lambda t: t and 'LocalBusiness' in t)
        if not existing:
            local_schema = soup.new_tag('script', type='application/ld+json')
            local_schema.string = '''{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Argamassa Baritada - Baritada Expert",
  "image": "https://www.marketsite.com.br/logo.png",
  "@id": "https://www.marketsite.com.br/",
  "url": "https://www.marketsite.com.br/",
  "telephone": "+55-11-99999-9999",
  "priceRange": "R$ 45 - R$ 85",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "BR",
    "addressRegion": "Brasil"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -23.5505,
    "longitude": -46.6333
  },
  "areaServed": {
    "@type": "Country",
    "name": "Brasil"
  },
  "sameAs": [],
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "opens": "08:00",
    "closes": "18:00"
  }
}'''
            head = soup.find('head')
            if head:
                head.append(local_schema)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print("✓ LocalBusiness schema adicionado")
    except Exception as e:
        print(f"❌ Erro ao adicionar LocalBusiness schema: {e}")

def adicionar_article_schema_paginas_conteudo():
    """Adiciona Article schema para páginas de conteúdo"""
    paginas_artigo = [
        'o-que-e-argamassa-baritada.html',
        'como-aplicar-argamassa-baritada.html',
        'preco-argamassa-baritada.html'
    ]
    
    for pagina in paginas_artigo:
        filepath = f'/home/ubuntu/argamassa-baritada/{pagina}'
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                # Verificar se já tem Article schema
                existing = soup.find('script', type='application/ld+json', string=lambda t: t and 'Article' in t)
                if not existing:
                    title_tag = soup.find('title')
                    title_text = title_tag.string if title_tag else pagina.replace('.html', '').replace('-', ' ').title()
                    
                    article_schema = soup.new_tag('script', type='application/ld+json')
                    article_schema.string = f'''{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title_text}",
  "author": {{
    "@type": "Organization",
    "name": "Baritada Expert"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Baritada Expert",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://www.marketsite.com.br/logo.png"
    }}
  }},
  "datePublished": "2025-01-01",
  "dateModified": "2025-01-01",
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://www.marketsite.com.br/{pagina}"
  }},
  "keywords": "argamassa baritada, proteção radiológica, blindagem raio-x, laudo cnen"
}}'''
                    head = soup.find('head')
                    if head:
                        head.append(article_schema)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    print(f"✓ Article schema adicionado em {pagina}")
            except Exception as e:
                print(f"❌ Erro ao processar {pagina}: {e}")

def otimizar_meta_keywords():
    """Adiciona e otimiza meta keywords (ainda usado por alguns buscadores)"""
    keywords_por_pagina = {
        'index.html': 'argamassa baritada, cotação argamassa baritada, laudo cnen, blindagem raio-x, proteção radiológica, sulfato de bário',
        'o-que-e-argamassa-baritada.html': 'o que é argamassa baritada, composição argamassa baritada, barita, sulfato de bário, blindagem radiológica',
        'como-aplicar-argamassa-baritada.html': 'como aplicar argamassa baritada, aplicação argamassa baritada, passo a passo, manual aplicação',
        'preco-argamassa-baritada.html': 'preço argamassa baritada, quanto custa argamassa baritada, valor argamassa baritada, cotação',
        'rendimento-argamassa-baritada.html': 'rendimento argamassa baritada, consumo por m², calculadora argamassa, quantos sacos preciso'
    }
    
    for arquivo, keywords in keywords_por_pagina.items():
        filepath = f'/home/ubuntu/argamassa-baritada/{arquivo}'
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
                if meta_keywords:
                    meta_keywords['content'] = keywords
                else:
                    new_meta = soup.new_tag('meta', attrs={'name': 'keywords', 'content': keywords})
                    head = soup.find('head')
                    if head:
                        head.append(new_meta)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                print(f"✓ Keywords otimizadas: {arquivo}")
            except Exception as e:
                print(f"❌ Erro em {arquivo}: {e}")

# Executar todas as otimizações
print("=== Otimizando Metadados e Schema Markup ===\n")

print("--- Otimizando Title Tags ---")
otimizar_title_tags()

print("\n--- Adicionando LocalBusiness Schema ---")
adicionar_local_business_schema()

print("\n--- Adicionando Article Schema ---")
adicionar_article_schema_paginas_conteudo()

print("\n--- Otimizando Meta Keywords ---")
otimizar_meta_keywords()

print("\n✅ Otimizações de metadados e schema markup concluídas!")
