weight_of_anil = 83
weight_of_ari = 65
weight_of_ali = 100
max_kg_elevator = 200

print "Maximum KG for Elevator " + str(max_kg_elevator)
print "Max KG for Elevator is {}".format(max_kg_elevator)

print "Anil is {}KG, Ari is {}KG, Ali is {}KG".format(weight_of_anil,weight_of_ari,weight_of_ali)

sum_of_weights = weight_of_anil + weight_of_ari + weight_of_ali
print "This three people can use the elevator : {}".format(sum_of_weights <= max_kg_elevator)
print "Ari and Anil can use elevator : {} ".format((weight_of_anil + weight_of_ari) <= max_kg_elevator)
