from colorama import Fore, Back, Style

class PageUtils:

    @staticmethod
    def red_text(msg):
        return Fore.RED + msg + Style.RESET_ALL

    @staticmethod
    def green_text(msg):
        return Fore.GREEN + msg + Style.RESET_ALL

    @staticmethod
    def blue_text(msg):
        return Fore.BLUE + msg + Style.RESET_ALL

    @staticmethod
    def bright_text(msg):
        return Style.BRIGHT + msg + Style.RESET_ALL

    @staticmethod
    def back_white(msg):
        return Back.WHITE + msg + Style.RESET_ALL

    @staticmethod
    def print_error(msg):
        print(PageUtils.red_text("ERRO") + ": " + str(msg) + "\n")

    @staticmethod
    def print_sucesso(msg):
        print(PageUtils.green_text("SUCESSO") + ": " + str(msg) + "\n")

    @staticmethod
    def print_menu(num, msg):
        print(PageUtils.green_text(num) + " - " + msg)

    @staticmethod
    def titulo(msg: str):
        dece = "---: "
        decd = " :---"
        msg = dece + msg.upper() + decd
        print("\n" + PageUtils.bright_text(PageUtils.back_white(PageUtils.green_text(msg))))

    @staticmethod
    def insira_texto(msg):
        return PageUtils.green_text("Insira ") + msg + ":"

    @staticmethod
    def confirm():
        return input("Confirmar? (s/n): ").lower() == "s"

    @staticmethod
    def try_catch_error(msg, func, *args):
        try:
            result = func(*args)
            PageUtils.print_sucesso(msg) if msg else None
            return result
        except Exception as e:
            PageUtils.print_error(e)

        return None

    @staticmethod
    def float_input(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                PageUtils.print_error("Digite um número flutuante.")

    @staticmethod
    def int_input(msg):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                PageUtils.print_error("Digite um número inteiro.")

    @staticmethod
    def str_input(msg):
        inp = str(input(msg))
        inp = inp.strip()
        return inp
    
    @staticmethod
    def print_tabela(nomes, conteudos):
        espacos_colunas = [0] * len(nomes)
        offset = 5
        
        for conteudo in conteudos:
            for i in range(len(conteudo)):
                if len(str(conteudo[i])) + offset > espacos_colunas[i]:
                    espacos_colunas[i] = len(str(conteudo[i])) + offset
                if len(nomes[i]) + offset > espacos_colunas[i]:
                    espacos_colunas[i] = len(nomes[i]) + offset

        cabeçalho = ""
        for i in range(len(nomes)):
            cabeçalho += nomes[i].ljust(espacos_colunas[i])
        print(PageUtils.blue_text(cabeçalho))

        for conteudo in conteudos:
            linha = ""
            for i in range(len(conteudo)):
                linha += str(conteudo[i]).ljust(espacos_colunas[i])
            print(linha)
    
    @staticmethod
    def confirma_alteracao(suf, msg):
        return input(f"Deseja alterar {suf} {msg} ? (s/n):").lower() == "s"