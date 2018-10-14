%--------------------------------------------------------------------------

%Path Determination Algorithm Prototype

%Project D.R.A.G.O.N. Navigation Software

%Proprietary Information enclosed


%Script generates shortest path given set grid and obstacles using three
%different algorithms to compare accuracy and computation time. The
%algorithms used include the following:

%                            -Dijkstra's Algorithm
%                            -A* Algorithm
%                            -D* Algorithm

%Inputs (ideally):
%                            -Topo map with nodes/obstacles
%                            -Heat map (science weighting)
%                            -Constraints
%                            -Waypoints

%Outputs (ideally):
%                            -Ideal path for rover
%                            -Coordinates for rover command

%Created on 9/24/2018 by Ryan Stewart
%Edited on 10/3/2018 by Ryan Stewart

%--------------------------------------------------------------------------

%Clean house
close all;clearvars;clc;

map = zeros(4,4);


Start = [1 1]; End = [4 4]; %set start and end points for test
open_list = Start; %set open queue 
closed_list = []; %set closed queue 
g(1) = 0; h(1) = hcost(Start,End); %set initial costs 

f(1) = g(1) + h(1); %full nodal cost for start

cl_count = 1; %closed list counter --> testing this for right now

iter = 1; %iter for g cost function --> still in testing 
while isempty(open_list) == 0
    
    idx = find(min(f)); %find index of node of minimum cost
    
    current_node = open_list(idx); %pull corresponding node
    
    if current_node == End %if this is the end, we can stop
        break 
    end
    
    open_list(idx) = []; %remove node from open list
    closed_list(cl_count) = current_node; %add node to closed list
    
    children = child(current_node,map); %find children of current node
    
    for i = 1:length(children);
        
        Child = children(i,:);
        
        if ismember(Child,closed_list,'rows')  %check if child node has been checked
            continue
        end
        
        cost = g(iter) + pdist2(current_node,Child);
        
        if 
            
        elseif
            
        elseif
            
        end
        
        
        
    end
    
    
    
    
end


