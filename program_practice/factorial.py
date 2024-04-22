# def factt(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i

#     return fact

# n=int(input("Enter any number:-"))
# print(factt(n))
# ==================resursion=====================================
def factt(n):
    # fact=1
    # for i in range(1,n+1):
    #     fact=fact*i

    return n*factt(n-1)

n=int(input("Enter any number:-"))
print(factt(n))