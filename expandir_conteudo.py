import os
from bs4 import BeautifulSoup

# --- Funções de Reescrita de Conteúdo ---

def expandir_conteudo_o_que_e(soup):
    """Expande o conteúdo da página 'O que é Argamassa Baritada'."""
    article = soup.find('article', class_='article-content')
    if not article:
        return soup

    # Adicionar mais detalhes na definição
    p_definicao = article.find('p', string=lambda t: t and 'Definição Técnica' in t.find_previous('h2').text)
    if p_definicao:
        p_definicao.string = 'A Argamassa Baritada, tecnicamente conhecida como reboco baritado, é um revestimento de alta densidade projetado especificamente para a blindagem de ambientes contra radiação ionizante, como salas de Raio-X, tomografia e medicina nuclear. Diferente de um reboco convencional, a argamassa baritada utiliza o mineral barita (sulfato de bário) em sua composição, o que lhe confere uma densidade excepcional (tipicamente 3.2 g/cm³), capaz de atenuar os fótons de radiação e garantir a segurança radiológica exigida pelas normas vigentes.'

    # Inserir tabela comparativa
    h2_composicao = article.find('h2', string='Composição: O Segredo da Proteção')
    if h2_composicao:
        tabela_html = '''
        <div class="table-container" style="margin-top:2rem;">
            <table>
                <thead>
                    <tr>
                        <th>Componente</th>
                        <th>Argamassa Baritada Certificada</th>
                        <th>Massa Comum + Barita (Incorreto)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Atenuação (Blindagem)</strong></td>
                        <td class="text-success">Garantida por laudo</td>
                        <td class="text-error">Não confiável, risco de vazamento</td>
                    </tr>
                    <tr>
                        <td><strong>Homogeneidade</strong></td>
                        <td class="text-success">Mistura industrial precisa</td>
                        <td class="text-error">Mistura desigual, pontos frágeis</td>
                    </tr>
                    <tr>
                        <td><strong>Aditivos Anti-fissura</strong></td>
                        <td class="text-success">Sim, polímeros elastizantes</td>
                        <td class="text-error">Não, alto risco de trincas</td>
                    </tr>
                     <tr>
                        <td><strong>Aprovação CNEN</strong></td>
                        <td class="text-success">Garantida com laudo</td>
                        <td class="text-error">Reprovação certa na vistoria</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p>A tentativa de "fazer a mistura em obra" é o erro mais comum e perigoso. Apenas a <strong>argamassa baritada</strong> produzida industrialmente garante a densidade e a homogeneidade necessárias para uma blindagem eficaz e a aprovação no levantamento radiométrico.</p>
        '''
        h2_composicao.insert_after(BeautifulSoup(tabela_html, 'html.parser'))

    return soup

def expandir_conteudo_index(soup):
    """Expande o conteúdo da página inicial.
    O foco é adicionar mais texto relevante e menções da palavra-chave.
    """
    # Expandir seção "Por que não arriscar"
    h2_laudo = soup.find('h2', string='Por que usar Argamassa Baritada com Laudo Certificado?')
    if h2_laudo:
        p_intro = h2_laudo.find_next_sibling('p')
        if p_intro:
            p_intro.string = 'A economia inicial na compra de uma argamassa baritada sem certificação pode resultar em custos até 10 vezes maiores com readequações de obra, interdição da sala e multas. O fiscal da Vigilância Sanitária, assim como o físico responsável pelo projeto radiométrico, exigirá o Laudo de Densidade do material e o Cálculo de Blindagem. Utilizar a argamassa baritada correta não é uma opção, é uma exigência legal e de segurança.'

    # Adicionar mais texto nos cards
    card_trincas = soup.find('h3', string='🚧 Evite Trincas')
    if card_trincas:
        p_card = card_trincas.find_next_sibling('p')
        if p_card:
            p_card.string = 'Uma parede de argamassa baritada não pode ter fissuras. Fornecedores homologados utilizam aditivos elastizantes que compensam a dilatação térmica e garantem uma superfície íntegra, mantendo a eficácia da blindagem radiológica por décadas.'

    return soup

def processar_arquivo(filepath):
    print(f"Processando: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        if os.path.basename(filepath) == 'index.html':
            soup = expandir_conteudo_index(soup)
        elif os.path.basename(filepath) == 'o-que-e-argamassa-baritada.html':
            soup = expandir_conteudo_o_que_e(soup)
        # Adicionar outras funções de expansão aqui

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"✓ Conteúdo expandido: {os.path.basename(filepath)}")

    except Exception as e:
        print(f"❌ Erro ao processar {filepath}: {e}")

# --- Execução ---
if __name__ == "__main__":
    arquivos_para_otimizar = [
        'index.html',
        'o-que-e-argamassa-baritada.html'
    ]

    for arquivo in arquivos_para_otimizar:
        caminho_completo = os.path.join('/home/ubuntu/argamassa-baritada', arquivo)
        if os.path.exists(caminho_completo):
            processar_arquivo(caminho_completo)
        else:
            print(f"⚠️ Arquivo não encontrado: {caminho_completo}")

    print("\n✅ Processo de expansão de conteúdo finalizado.")

