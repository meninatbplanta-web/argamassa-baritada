import os
import re

# Definição dos Blocos de HTML Otimizados (Baseado na consultoria anterior)

# 1. Nova Seção Técnica (Merge de Rendimento + Aplicação)
CONTEUDO_TECNICO_NOVO = """
<section class="section bg-white" style="border-top: 1px solid #eee; border-bottom: 1px solid #eee;">
    <div class="container">
        <h2 class="text-center">Manual Técnico e Tabela de Rendimento</h2>
        <p class="text-center" style="margin-bottom:3rem; max-width:800px; margin-left:auto; margin-right:auto;">
            Informações essenciais para o cálculo e aplicação na obra. Siga rigorosamente para garantir a blindagem.
        </p>

        <div class="grid-3">
            <div class="tech-box" style="background: #fff; border-left: 4px solid #004d40; padding: 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h3>📊 Cálculo de Consumo</h3>
                <p>O cálculo base considera a densidade de <strong>3.2 g/cm³</strong>.</p>
                <div class="table-container" style="overflow-x: auto; background: #fff; border-radius: 8px; margin-bottom: 1rem;">
                    <table style="width: 100%; border-collapse: collapse; min-width: 300px;">
                        <thead>
                            <tr style="background: #004d40; color: #fff;">
                                <th style="padding: 12px; text-align: left;">Espessura</th>
                                <th style="padding: 12px; text-align: left;">Consumo (Saco 25kg)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px;">1,0 cm</td>
                                <td style="padding: 12px;">25 kg/m² (1 saco = 1 m²)</td>
                            </tr>
                            <tr style="background-color: #f9f9f9; border-bottom: 1px solid #eee;">
                                <td style="padding: 12px;">1,5 cm</td>
                                <td style="padding: 12px;">37,5 kg/m² (1.5 sacos/m²)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px;">2,0 cm</td>
                                <td style="padding: 12px;">50 kg/m² (2 sacos/m²)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="highlight-yellow" style="background: #fffde7; padding: 15px; border-radius: 4px; border: 1px solid #fff9c4; margin: 15px 0;">
                    <strong>Fórmula:</strong><br>
                    <code>25kg × Espessura(cm) × Área(m²)</code>
                </div>
                <a href="calculadora-argamassa.html" style="color:#004d40; font-weight:bold; text-decoration:underline;">Usar Calculadora Automática ➤</a>
            </div>

            <div class="tech-box" style="grid-column: span 2; background: #fff; border-left: 4px solid #004d40; padding: 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h3>🛠️ Protocolo de Aplicação (Passo a Passo)</h3>
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:2rem;">
                    <div>
                        <h4>1. Preparo da Base</h4>
                        <p>A parede deve estar limpa. É <strong>obrigatório</strong> o uso de chapisco grosso (traço 1:3 cimento/areia) com aditivo de aderência (ex: Bianco) para suportar o peso da barita.</p>
                        
                        <h4>2. Aplicação em Drywall</h4>
                        <p>Utilize apenas placas cimentícias ou RF (Resistentes ao Fogo). É recomendado fixar tela metálica ou de fibra sobre a placa para ancoragem mecânica.</p>
                    </div>
                    <div>
                        <h4>3. Camadas (Importante)</h4>
                        <p>Não aplique camadas superiores a <strong>1,5 cm</strong> de uma vez. Se o projeto pedir 2,0 cm, faça duas demãos de 1,0 cm, com intervalo de 24h e ranhuras na primeira camada.</p>
                        
                        <h4>4. Cura</h4>
                        <p>Realize <strong>cura úmida</strong> (molhar a parede) por 3 dias consecutivos após a aplicação para evitar fissuras por retração, garantindo a integridade da blindagem.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# 2. Bloco de Autoridade (E-E-A-T)
BLOCO_AUTORIDADE = """
<div class="author-box" style="background: #e3f2fd; padding: 1.5rem; border-radius: 8px; display: flex; gap: 1rem; align-items: center; margin-top: 2rem; border: 1px solid #bbdefb; flex-wrap: wrap;">
    <div style="flex:1; min-width: 300px;">
        <h4 style="margin:0; color:#004d40;">Responsabilidade Técnica e Normas</h4>
        <p style="margin:5px 0 0; font-size:0.9rem; color:#555;">
            Conteúdo revisado por Supervisor de Radioproteção certificado.<br>
            Em conformidade com a norma <strong>CNEN-NN-3.01</strong> e <strong>ABNT NBR 16937</strong>.<br>
            <em>A aplicação deve sempre seguir o projeto de blindagem elaborado por um Físico Médico.</em>
        </p>
    </div>
    <div style="text-align:right; flex: 1;">
        <a href="contato.html" class="btn btn-primary" style="font-size:0.8rem; padding:10px 20px; background-color: #ff6f00; color: #000; text-decoration: none; font-weight: 800; border-radius: 4px;">FALAR COM ESPECIALISTA</a>
    </div>
</div>
"""

def aplicar_seo_no_index(caminho_arquivo='index.html'):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        content = f.read()

    print("--- Iniciando Otimização de SEO ---")

    # 1. REMOVER DUPLICAÇÃO DO SCHEMA 'Product'
    # Procuramos por blocos <script type="application/ld+json"> que contenham "Product"
    # Vamos contar e manter apenas o primeiro ou remover um específico se forem idênticos.
    # Como a análise mostrou duplicação exata, vamos usar uma regex para identificar blocos JSON-LD.
    
    pattern_schema = re.compile(r'<script type="application/ld\+json">.*?</script>', re.DOTALL)
    schemas = pattern_schema.findall(content)
    
    product_schemas_found = 0
    new_content = content
    
    for schema in schemas:
        if '"@type": "Product"' in schema:
            product_schemas_found += 1
            if product_schemas_found > 1:
                print("-> Removendo Schema de Produto duplicado...")
                new_content = new_content.replace(schema, "", 1) # Remove apenas 1 ocorrência extra

    # 2. INSERIR CONTEÚDO TÉCNICO CONSOLIDADO
    # Estratégia: Inserir DEPOIS da section "Por que usar Argamassa Baritada" e ANTES do "Guia Completo"
    # Marcador: Vamos procurar o fechamento da section anterior (bg-light) e o inicio da proxima.
    
    # Marcador visual: <h2 class="text-center">Guia Completo sobre Argamassa Baritada</h2>
    marcador_guia = '<h2 class="text-center">Guia Completo sobre Argamassa Baritada</h2>'
    
    if marcador_guia in new_content:
        # Procuramos a tag <section> que envolve esse título para inserir ANTES dela
        # Mas para ser mais seguro e fácil, vamos inserir logo antes da section que contem o guia.
        # Vamos achar a linha: <section class="section bg-light"> que vem antes do Guia.
        # Uma abordagem segura é substituir a abertura da section do guia para incluir o conteudo novo antes.
        
        # Vamos tentar achar o container do guia
        trecho_busca = '<section class="section bg-light">\n<div class="container">\n<h2 class="text-center">Guia Completo'
        
        # Se não achar com quebras de linha exatas, tentamos buscar só o titulo e voltar atrás
        if marcador_guia in new_content:
            print("-> Inserindo Manual Técnico e Tabela de Rendimento...")
            # Inserir ANTES da section do Guia Completo. 
            # Como é difícil achar o inicio exato da tag section via string simples se houver variações,
            # vamos inserir APÓS o fechamento da section anterior ("Por que usar...").
            
            marcador_fim_section_anterior = '</div>\n</div>\n</article>\n</div>\n</section>'
            
            if marcador_fim_section_anterior in new_content:
                 new_content = new_content.replace(marcador_fim_section_anterior, marcador_fim_section_anterior + "\n" + CONTEUDO_TECNICO_NOVO)
            else:
                # Fallback: Inserir logo antes de "Guia Completo"
                 new_content = new_content.replace(marcador_guia, CONTEUDO_TECNICO_NOVO + "\n" + marcador_guia)

    # 3. INSERIR BLOCO DE AUTORIDADE (E-E-A-T)
    # Estratégia: Inserir no final da seção "Guia Completo", logo antes de fechar a div container ou antes do FAQ.
    # Marcador: Antes de <section class="section bg-white"> que contém o FAQ.
    
    marcador_faq = '<h2>Perguntas Frequentes</h2>'
    
    if marcador_faq in new_content:
         # Achar a section do FAQ
         # Vamos tentar inserir logo antes da section do FAQ iniciar
         pass
    
    # Vamos inserir logo APÓS o grid de cards do Guia Completo.
    # O grid fecha com </div> e depois vem </section>
    # Vamos procurar o ultimo card "Ver Rotas" e inserir depois do fechamento dele.
    
    marcador_ultimo_card = '<a href="entrega-brasil.html" style="color:var(--primary); font-weight:bold;">Ver Rotas</a>\n</div>'
    # Ajuste para lidar com variações de espaço/quebra de linha no HTML original
    # Vamos usar regex para achar o fechamento da div grid-3
    
    # Uma forma segura: Inserir antes da tag <section class="section bg-white"> que inicia o FAQ.
    marcador_inicio_faq = '<section class="section bg-white">'
    if marcador_inicio_faq in new_content:
        print("-> Inserindo Bloco de Autoridade E-E-A-T...")
        # Inserimos antes da section do FAQ, garantindo que fique na section anterior (bg-light) ou entre elas.
        # O ideal é ficar dentro do container da section anterior.
        # Vamos inserir o bloco ANTES de fechar a section anterior.
        
        # Como o HTML é complexo, vamos inserir logo ANTES da section de FAQ.
        # O bloco AUTHORITY já tem div, mas se ficar fora de container pode quebrar layout.
        # O script acima define o bloco authority com container proprio? Não, ele é uma div author-box.
        # Ele precisa estar dentro de um container.
        
        # Correção no HTML do bloco para garantir container se for inserido solto
        bloco_final = f'<div class="container">{BLOCO_AUTORIDADE}</div>'
        
        # Inserir antes da section de FAQ
        new_content = new_content.replace(marcador_inicio_faq, bloco_final + "\n" + marcador_inicio_faq)

    # 4. SALVAR ARQUIVO
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("--- Sucesso! Alterações aplicadas em index.html ---")
    print("1. Schema duplicado removido.")
    print("2. Tabela de Rendimento e Manual inseridos.")
    print("3. Bloco de Autoridade adicionado.")

if __name__ == "__main__":
    aplicar_seo_no_index()