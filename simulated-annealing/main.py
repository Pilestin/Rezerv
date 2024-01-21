import math
import numpy as np 
import random
# Routing için matrisin oluşturulması 

x1 = [ 0, 10, 15, 20, 25, 30] 
x2 = [10,  0, 35, 25, 20, 15]
x3 = [15, 35,  0, 30, 10,  5]
x4 = [20, 25, 30,  0,  5, 10]
x5 = [25, 20, 10,  5,  0,  8]
x6 = [30, 15,  5, 10,  8,  0]

distance_matrix = [x1,x2,x3,x4,x5,x6]

def GenerateNeighborSolution(currentSolution: list):
    # Çözüm kopyalanır
    newSolution = currentSolution.copy() 
    # rastgele iki index seçilir. 
    index1, index2 = random.sample(range(len(newSolution)), 2) 
    # Bu seçilen iki rastgele index yer değiştirilir ve yeni çözüm döndürülür
    newSolution[index1], newSolution[index2] = newSolution[index2], newSolution[index1]
    return newSolution 

def EvaluateEnergy(currentSolution: list):
    
    totalEnergy = 0 
    # Çözümdeki şehirler arası mesafeler toplanır
    for i in range(len(currentSolution)-1):
        totalEnergy += distance_matrix[currentSolution[i]][currentSolution[i+1]]
    
    # Eğer başladığımız noktaya geri dönmemiz gerekir ise burayı da eklemeliyiz: 
    # total_energy += distance_matrix[solution[-1]][solution[0]]
    return totalEnergy
    
def AcceptanceProbability(currentEnergy: float , newEnergy: float, temperature: float):
    
    # Enerji farkları kontrol edilir
    deltaE = currentEnergy - newEnergy
    # Termodinamik bağıntısına göre kabul edilme olasılığı döndürülür
    return math.exp(deltaE / temperature)


def SimulatedAnnealing(initialSolution: list, initialTemperature: int, coolingRate: float, maxIterations: int):
    # ilk çözüm en iyi çözüm varsayımı ile başlanır
    currentSolution = initialSolution.copy()
    bestSolution = currentSolution.copy() 
    temperature = initialTemperature
    
    for i in range(maxIterations):        
        newSolution = GenerateNeighborSolution(currentSolution)
        newEnergy = EvaluateEnergy(newSolution)
        currentEnergy = EvaluateEnergy(currentSolution)
        
        if (newEnergy < currentEnergy) or AcceptanceProbability(currentEnergy, newEnergy, temperature) > random.uniform(0, 1) : 
            currentSolution = newSolution
            
        if newEnergy < EvaluateEnergy(bestSolution):
            bestSolution = newSolution
            temperature *= coolingRate
        
    return bestSolution


def main():
    # Başlangıç çözümü (örneğin, şehirleri sırayla ziyaret et)
    initialSolution = [0, 1, 2, 3, 4, 5]
    # Diğer parametreler
    initialTemperature = 10000
    coolingRate = 0.95
    maxIterations = 50
    _bestSolution = SimulatedAnnealing(initialSolution, initialTemperature, coolingRate, maxIterations)
    bestSolution = [city + 1 for city in _bestSolution]
    print(f"Sıcaklık : {initialTemperature} Soğutma Oranı : {coolingRate} İterasyon Sayısı : {maxIterations}")
    print("En iyi çözüm : ", bestSolution)
    print("Enerji Maliyeti : ", EvaluateEnergy(_bestSolution))
    
    
main()