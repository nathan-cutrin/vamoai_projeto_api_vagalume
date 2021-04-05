from model import BuscaAPI


class CtrlAPI:
    def __init__(self):
        self.model = BuscaAPI(tipo_de_rank='art')

    def formatacao_rank_geral(self):
        rank = self.model.rank_geral()
        print(rank)

        for elemento in rank:
            print(f"Nome: {elemento['name']}, visualizações únicas: {elemento['uniques']}, "
                  f"total de visualizações: {elemento['views']}\n")
        return rank

        # rank = BuscaAPI(self.tipo_de_rank)
        # print(rank)
        # rank_normal = rank.rank_geral()
        # print(rank_normal)
        # return rank_normal


a = CtrlAPI()
a.formatacao_rank_geral()
