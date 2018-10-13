%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%Cost function for A* Algorithm 

%Generates cost of studied node based on distance from start node

%Inputs:            
%               -Current node
%               -Starting node

%Outputs:
%               -Cost of node

%Created by Ryan Stewart on 10/6/2018
%Edited by Ryan Stewart on 10/6/2018

%--------------------------------------------------------------------------

function g = g_cost(current_node,start_node)

g = pdist2(current_node,start_node);

end


