import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('sonar.py', 'test.py')                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python3 {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=2)                                                        
pool.map(run_process, processes)