%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%Heuristic function for A* Algorithm 

%Generates crows distance to ending location, receives node being studied
%and the final node as 

%Inputs:
%                  -Node studied = node_c
%                  -Ending node  = node_end

%Outputs:
%                  -Heuristic cost of point

%Created by Ryan Stewart on 10/2/2018
%Edited by Ryan Stewart on 10/2/2018

%--------------------------------------------------------------------------


function h = h_cost(node_c,node_end)

h = pdist2(node_c,node_end);
%h = 0;

end

