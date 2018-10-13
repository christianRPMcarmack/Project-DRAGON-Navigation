%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%Jump checking function for object detection 

%Generates flag value for whether or not current path will cross over an
%object in the map

%Inputs:
%               -dist_x -> distance from current node to desired x node
%               -dist_y -> distance from current node to desired y node
%               -grid map for rover
%               -current node

%Outputs:
%               -Flag -> Flag == 1 is good path, Flag == 0 implies obstacle

%Created by Ryan Stewart on 10/8/2018
%Edited by Ryan Stewart on 10/8/2018

%Directly uses method implemented by Einer Ueland from Mathworks website

%Open source code: https://www.mathworks.com/matlabcentral/fileexchange/56877-a-astar-a-star-search-algorithm-easy-to-use

%--------------------------------------------------------------------------


function Flag = obstacle_jump(dist_x,dist_y,current_node,map)
Flag = 1;

current_nodex = current_node(1); current_nodey = current_node(2);  
        
    J_Cells = 2*max(abs(dist_x),abs(dist_y))-1; %Max number of jumped cells depends on the scale factor 
                                                %3 for 16, 5 for 32, etc...
    for idx = 1:J_Cells
        X = round(idx*dist_x/J_Cells); %fractionally move across all cells crossed by path 
        Y = round(idx*dist_y/J_Cells);

        if (map(current_nodex+X,current_nodey+Y) == 1)
            Flag = 0; %If object exists in path cell, set flag to 0 to ignore
        end

    end
 


end

