def solution(tickets):
    answer = []
    
    ticket = dict()
    
    for (a, b) in tickets:
        if a in ticket:
            ticket[a].append(b)
        else:
            ticket[a] = [b]
            
    for i in ticket.keys():
        ticket[i].sort(reverse=True)
    
    stack = ['ICN']
    while stack:
        top = stack[-1]
        
        if top not in ticket or not ticket[top]:
            answer.append(stack.pop())
        else:
            stack.append(ticket[top].pop())
            
    return answer[::-1]