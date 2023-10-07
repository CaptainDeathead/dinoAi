import neat
import os
import pickle
from main import getInfo
import pyautogui as pag
import time

def eval_genomes(genomes, config):
    nets = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)

    inc = 0.1
    i=0
    for genome_id, genome in genomes:
        stime = time.time()
        pag.click(1000, 500)
        #pag.hotkey("ctrl", "r")
        #pag.press("space")
        e = 300
        a = 600
        print('eeee')
        bre = 0
        while True:
            bre += 1
            things = getInfo(e)
            thingsa = getInfo(a)
            if things[0] == "e":
                etime = time.time()
                genome.fitness = etime - stime
                break
            else:
                for z in thingsa:
                    things.append(z)
                things.append(bre)
                #things.append(inc)
                try:
                    output = nets[i].activate((things))
                    if output[0] > 0.5:
                        pag.keyDown("space")
                except Exception as xe:
                    print(xe)
            #e+=inc
        i+=1

    best_genome = None
    for genome_id, genome in genomes:
        if best_genome == None or genome.fitness > best_genome.fitness:
            best_genome = genome

    with open("ai.pickle", "wb") as f:
        pickle.dump(best_genome, f)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(20))

    winner = p.run(eval_genomes, 1000)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)