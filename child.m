%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%Find children surrounding current node for possible testing

%Generates node x and y coordinates for any grid points in contact with the
%node being studied
%                           -Node studied = node_c
%                           -Scale for how many neighbors to be studied 

%Outputs children nodes of current node

%Created by Ryan Stewart on 10/2/2018
%Edited by Ryan Stewart on 10/7/2018

%Converted to use neighbor formula generated by Einar Ueland on Mathworks
%website --> https://www.mathworks.com/matlabcentral/fileexchange/56877-a-astar-a-star-search-algorithm-easy-to-use

%--------------------------------------------------------------------------

function children = child(node_c,scale)

%Scale of 1 = 8 neighbors (vanilla A*), 2 = 16 neighbors, 3 = 32 neighbors,
%and so on...

NeighborCheck = ones(2*scale+1);
Dummy = 2*scale+2;
Mid = scale+1;
for i=1:scale-1
NeighborCheck(i,i)=0;
NeighborCheck(Dummy-i,i)=0;
NeighborCheck(i,Dummy-i)=0;
NeighborCheck(Dummy-i,Dummy-i)=0;
NeighborCheck(Mid,i)=0;
NeighborCheck(Mid,Dummy-i)=0;
NeighborCheck(i,Mid)=0;
NeighborCheck(Dummy-i,Mid)=0;
end
NeighborCheck(Mid,Mid)=0;

[row, col]=find(NeighborCheck==1);
Neighbors=[row col]-(scale+1);

children = Neighbors+node_c;



% children = zeros(8,2); %max of 8 neighbors
% 
% bounds = size(map);
% 
% save_idx = 1;
% 
% for idx = -1:1
%     x_child = node_c(1)+idx;
%     for idy = 1:-1:-1
%         if idx == 0 && idy == 0
%             continue
%         end
%     y_child = node_c(2)+idy;
%         if x_child <1 || y_child <1 || y_child >bounds(1) || x_child >bounds(2)
%             continue
%         end
%     children(save_idx,:) = [x_child y_child];
%     save_idx = save_idx + 1;        
%     end
% 
% end
% children = children(any(children,2),:);





end
