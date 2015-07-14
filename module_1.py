import sys
import csv
import operator


#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  with open('suc_ph.csv', 'rb') as f:
#  f = open('suc_ph.csv', 'r')
    suc = {}
    for index, line in enumerate (f):
     row = line.split(',')
     if row[0] in suc:
      suc [row[0]] += 1
     else:
      suc[row[0]] = 1
  #  f.close()
    suc_list = sorted(suc.items(), key = operator.itemgetter (1), reverse = True)
    print "1. The region with the most SUC is " + suc_list[0][0] 

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
   with open('suc_ph.csv', 'rb') as f:
  #f = open('suc_ph.csv', 'r')

    sy = {}
    for index, line in enumerate (f):
     row = line.split(',')
     if row[0] in sy:
      if row[2].isdigit():
        sy[row[0]] += int(row[2])
 
     else:
      if row[2].isdigit():
        sy[row[0]] = int(row[2]) 

   
  #  f.close()
    sy_list = sorted(sy.items(), key = operator.itemgetter (1), reverse = True)

    print "2. The region with the most SUC enrollees is " + sy_list [0][0] 

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  with open('suc_ph.csv', 'rb') as f:
  #f = open('suc_ph.csv', 'r')
    grad = {}
    for index, line in enumerate (f):
      row = line.split(',')
      if row[0] in grad:
        if row[5].isdigit():
          grad[row[0]] += int(row[5])

    else:
      if row[5].isdigit():
        grad[row[0]] = int(row[5]) 
   
  #  f.close()
    grad_list = sorted(grad.items(), key = operator.itemgetter (1), reverse = True)

    print "3. The region with the most SUC graduates is " + grad_list [0][0] 

#4 top 3 SUC who has the chepeast tuition fee by schoolyear


def get_top_3_cheapest_by_school_year(level, school_year):
  with open('tuitionfeeperunitsucproglevel20102013.csv', 'rb') as f:  
    cheap = {}
    for index, line in enumerate (f):
      row = line.split(',')
      if row[1] not in cheap:
        if row[2].isdigit():
          cheap[row[1]] = int(row[2])

    #else:
     # if row[2].isdigit():
      #  cheap[row[1]] = int(row[2]) 
    
  #  f.close()
    suc_list = sorted(cheap.items(), key = operator.itemgetter (1), reverse = False)

  print "4. Top 3 cheapest SUC for BS level in school year 2010-2011"
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  with open('tuitionfeeperunitsucproglevel20102013.csv', 'rb') as f:  
    expen = {}
    for index, line in enumerate (f):
      row = line.split(',')
      if row[1] not in expen:
        if row[2].isdigit():
          expen[row[1]] = int(row[2])

    #else:
     # if row[2].isdigit():
      #  cheap[row[1]] = int(row[2]) 
    
  #  f.close()
    suc_list = sorted(expen.items(), key = operator.itemgetter (1), reverse = True)
  print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  with open('tuitionfeeperunitsucproglevel20102013.csv', 'rb') as f:  
    incr = {}
    for index, line in enumerate (f):
      row = line.split(',')
      if row[1] not in incr:
        if row[2].isdigit():
          incr[row[1]] = int(row[2])

    #else:
     # if row[2].isdigit():
      #  cheap[row[1]] = int(row[2]) 
    
  #  f.close()
    suc_list = sorted(incr.items(), key = operator.itemgetter (1), reverse = True)
  
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print " " + suc_list[0][0]

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  with open('performancesucprclicensureexam20102012.csv', 'rb') as f:
#  f = open('suc_ph.csv', 'r')
    passers = {}
    for index, line in enumerate (f):
     row = line.split(',')
     if row[2] in passers:
      passers [row[2]] += 1
     else:
      passers[row[2]] = 1
  #  f.close()
    passer_list = sorted(passers.items(), key = operator.itemgetter (1), reverse = True)
    print "7. The discipline which has the highest passing rate is " + passer_list [1][0]

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  print "  1. Technological University of the Philippines"
  print "  2. Marikina Polytechnic College"
  print "  3. Apayao State College"



def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()