# -*- coding: utf-8 -*-

'''
Created on 13/04/2013

@author: ThiagoP
'''

class Calc(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.salary = 0.0
        self.semanal_journey = 0
        self.week_days = []
        self.transport_cost = 0.0 
        self.transport_xtimes_day = 0
        self.extra_hour_perc = 0.0 
    
   
    def initFromFuncionario(self, f):
        pass
   
   
    def init(self, salary, semanal_journey, transport_cost=0, transport_xtimes_day=0, week_days = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab'], extra_hour_perc=50):
        self.salary = float(salary)
        
        if int(semanal_journey) > 44:
            raise Exception("A jornada de trabalho semanal não pode ser superior a 44 horas.")
        else:
            self.semanal_journey = int(semanal_journey)
        
        if len(week_days) > 6:
            raise Exception("Funcionário deve ter, obrigatoriamente, um dia de folga na semana.")
        else:
            self.week_days = week_days
        
        self.transport_cost = float(transport_cost)
        self.transport_xtimes_day = int(transport_xtimes_day)
        self.extra_hour_perc = float(extra_hour_perc)
        
    
    def worked_hour(self):
        """
        Retorna o valor da hora trabalhada pelo empregado (salário dividido pelas horas trabalhadas no mês)
        """
        return (self.salary / (self.semanal_journey * 5))
    
    
    def extra_hour(self):
        return (self.salary / (self.semanal_journey * 5)) * (1 + (self.extra_hour_perc/100))
    
    
    def transport_month(self):
        return ((self.transport_cost * self.transport_xtimes_day) * (len(self.week_days) * 5))
    
    
    def transport_discount(self):
        transport_cost = self.transport_month()
        discount = self.salary * 0.06
        
        if transport_cost <= discount:
            ret = transport_cost
        else:
            ret = discount
            
        return ret
    
    
    def transport_employer(self):
        transport_cost = self.transport_month()
        discount = self.salary * 0.06
        
        if transport_cost > discount:
            ret = transport_cost - discount
        else:
            ret = 0
            
        return ret
    
    
    def inss(self):
        return self.salary * .20
    
    
    def inss_employee(self):
        #TODO: Jogar essa lógica pra uma tabela no banco pra evitar alterar código quando as aliquotas mudarem
        if self.salary <= 1247.70:
            ret = self.salary * .08 
        elif self.salary > 1247.70 and self.salary <= 2079.50:
            ret = self.salary * .09
        elif self.salary > 2079.50 and self.salary <= 4159:
            ret = self.salary * .11
        else:
            ret = 4159 * .11
            
        return ret
    
    
    def inss_employer(self):
        #TODO: Jogar essa lógica pra uma tabela no banco pra evitar alterar código quando as aliquotas mudarem
        if self.salary <= 1247.70:
            ret = self.salary * .12 
        elif self.salary > 1247.70 and self.salary <= 2079.50:
            ret = self.salary * .11
        elif self.salary > 2079.50 and self.salary <= 4159:
            ret = self.salary * .9
        else:
            ret = 4159 * .9
            
        return ret
    
    
    def fgts(self):
        return self.salary * .08
    
if __name__ == "__main__":
    c = Calc()
    c.init(678, 44, transport_cost=2.3, transport_xtimes_day=2)
    
    print "----------------- Rendimentos ---------------------"
    print "Salário Bruto: %.2f" %c.salary
    print "--Valor da hora trabalhada: %.2f" %c.worked_hour()
    print "--Valor da hora extra: %.2f" %c.extra_hour()
    print "\n----------------- Transporte ----------------------"
    print "Total mensal de transporte: %.2f" %c.transport_month()
    print "--Desconto de transporte: %.2f" %c.transport_discount()
    print "--Transporte para o empregador: %.2f" %c.transport_employer()
    print "\n----------------- Previdência ---------------------"
    print "INSS: %.2f " %c.inss()
    print "--Parcela empregado: %.2f " %c.inss_employee()
    print "--Parcela empregador: %.2f " %c.inss_employer()
    print "FGTS: %.2f " %c.fgts()