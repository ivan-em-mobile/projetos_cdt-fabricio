import tkinter as tk
from tkinter import messagebox

# --- Documentação do Código ---
# Este programa implementa o Jogo da Velha com interface gráfica usando Tkinter.
# A lógica de jogo é encapsulada na classe 'TicTacToeApp'.

class TicTacToeApp:
    """
    Classe principal para o Jogo da Velha com GUI.
    Gerencia a interface, o estado do jogo e a interação.
    """
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Velha (Tic-Tac-Toe)")
        
        # 1. Configuração do Estado do Jogo
        self.tabuleiro = [' ' for _ in range(9)]
        self.jogador_atual = 'X'
        self.jogo_ativo = True
        
        # 2. Configuração da Interface
        self.botoes = [] # Lista para armazenar os 9 botões do tabuleiro
        self.criar_widgets()

    def criar_widgets(self):
        """ Cria e posiciona todos os elementos da interface (rótulos e botões). """

        # Rótulo de Mensagem (mostra o turno ou o resultado)
        self.label_mensagem = tk.Label(self.master, text=f"Vez do Jogador {self.jogador_atual}", font=('Arial', 14, 'bold'))
        self.label_mensagem.grid(row=0, column=0, columnspan=3, pady=10)

        # Criação dos Botões do Tabuleiro
        for i in range(9):
            # i // 3 calcula a linha (0, 1, 2)
            # i % 3 calcula a coluna (0, 1, 2)
            
            botao = tk.Button(self.master, 
                                text=' ', 
                                font=('Arial', 24, 'bold'), 
                                width=5, 
                                height=2,
                                bg='#f0f0f0', # Cor de fundo leve
                                command=lambda i=i: self.fazer_jogada(i)) # Chama fazer_jogada com o índice
            
            # Posiciona o botão na grade
            botao.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5) 
            self.botoes.append(botao)
            
        # Botão de Reiniciar Jogo
        self.botao_reiniciar = tk.Button(self.master, 
                                         text="Reiniciar Jogo", 
                                         font=('Arial', 12),
                                         command=self.reiniciar_jogo)
        self.botao_reiniciar.grid(row=5, column=0, columnspan=3, pady=20)


    def fazer_jogada(self, posicao):
        """ 
        Executada quando um botão é clicado. Processa a jogada.
        :param posicao: O índice do tabuleiro (0-8) que foi clicado.
        """
        if self.jogo_ativo and self.tabuleiro[posicao] == ' ':
            # 1. Atualiza o estado do jogo e a interface
            self.tabuleiro[posicao] = self.jogador_atual
            self.botoes[posicao]['text'] = self.jogador_atual
            
            # Muda a cor do texto para melhor visualização
            cor = 'blue' if self.jogador_atual == 'X' else 'red'
            self.botoes[posicao]['fg'] = cor 

            # 2. Verifica as condições de fim de jogo
            if self._verificar_vitoria():
                self.label_mensagem.config(text=f"Parabéns! O jogador {self.jogador_atual} VENCEU!")
                self.jogo_ativo = False
                self._desabilitar_botoes()
            elif self._verificar_empate():
                self.label_mensagem.config(text="O jogo terminou em EMPATE!")
                self.jogo_ativo = False
            else:
                # 3. Troca o jogador
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                self.label_mensagem.config(text=f"Vez do Jogador {self.jogador_atual}")

    
    def _verificar_vitoria(self):
        """ Verifica se o jogador atual venceu. (Lógica similar à do código original) """
        vitorias = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        for combo in vitorias:
            if all(self.tabuleiro[i] == self.jogador_atual for i in combo):
                # Opcional: Destacar os botões vencedores
                for i in combo:
                    self.botoes[i].config(bg='lightgreen')
                return True
        return False
        
    def _verificar_empate(self):
        """ Verifica se o jogo terminou em empate. """
        return ' ' not in self.tabuleiro
        
    def _desabilitar_botoes(self):
        """ Desabilita todos os botões após o fim do jogo. """
        for botao in self.botoes:
            botao.config(state=tk.DISABLED)

    def reiniciar_jogo(self):
        """ Redefine o estado do jogo e a interface para um novo jogo. """
        self.tabuleiro = [' ' for _ in range(9)]
        self.jogador_atual = 'X'
        self.jogo_ativo = True
        
        # Resetar a aparência e o estado dos botões
        for i, botao in enumerate(self.botoes):
            botao.config(text=' ', 
                         state=tk.NORMAL, 
                         bg='#f0f0f0', 
                         fg='black') # Volta para a cor padrão
            
        self.label_mensagem.config(text=f"Vez do Jogador {self.jogador_atual}")


if __name__ == '__main__':
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Inicializa a aplicação
    app = TicTacToeApp(root)
    # Inicia o loop principal de eventos do Tkinter
    root.mainloop()