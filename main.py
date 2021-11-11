from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
#from quotes import get_quotes
#from news import find_hdline, test

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs + so_jobs
save_to_file(jobs)

#for i in get_quotes():
#  print(i.text)

#find_hdline()
#test()