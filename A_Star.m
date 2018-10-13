%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%Main A* Function for Project DRAGON

%Generates the shortest path between provided waypoints from start to end
%using A* with a user provided neighbor search factor

%Inputs: 
%               -Provided map
%               -Waypoints
%               -Neighbor Factor
%               -Start Point


%Outputs:
%               -Optimal path (X Y nodes format --> might need to change?)


%Created by Ryan Stewart on 10/11/2018 (separate function created)
%Edited by Ryan Stewart on 10/11/2018

%--------------------------------------------------------------------------


function optimal_f = A_Star(map,waypoints,NF,start)

[height,width] = size(map); %Pull map sizing information and preallocate arrays
G = zeros(height,width);
F = single(inf(height,width));
H = zeros(height,width);



open_list = zeros(height,width);closed_list = zeros(height,width); %open set
parent_X = zeros(height,width); parent_Y = zeros(height,width); %closed set
start_x = start(1); start_y = start(2);
closed_list(map==1) = 1; optimal_f = {}; %set objects and optimal cell array


for w = 1: length(waypoints)
    
    End_x = waypoints(w,1); End_y = waypoints(w,2); End = [End_x End_y]; %Pull end point from waypoints
    
        for idx = 1:height %generate heuristic matrix
            for idy = 1: width
                if map(idx,idy) == 0
                H(idx,idy) = h_cost([idx idy],[End_x End_y]); %call heuristic function  
                end
            end 
        end

        %set initial conditions for start and end and put start on open list
        F(start_x,start_y) = H(start_x,start_y);
        open_list(start_x,start_y) = 1;

        while 1 %isempty(open_list) == 0

            min_f = min(min(F)); %find location of minimum cost

            if min_f == inf %error check for if path cannot be generated
                disp('No optimal path! Ending algorithm!')
                Construct = 0;
                break
            end

            [current_nodex,current_nodey] =  find(F == min_f);%pull corresponding node

            if size(current_nodex,1) > 1 %save first index if multiple low cost iterations
                current_nodex = current_nodex(1);
            end

            if size(current_nodey,1) > 1
                current_nodey = current_nodey(1);
            end

            current_node = [current_nodex current_nodey]; %creat current node array

            if current_node == End  %#ok<BDSCI> %if this is the end, we can stop
                Construct = 1;
                break 
            end

            open_list(current_nodex,current_nodey) = 0;%remove node from open list
            F(current_nodex,current_nodey) = inf; %reset closed node score
            closed_list(current_nodex,current_nodey) = 1;

            children = child(current_node,NF); %find children of current node

            for i = 1:length(children)

                Child_x = children(i,1); Child_y = children(i,2); Child = [Child_x Child_y]; %set current child
                Flag = 1; %proto flag
                if Child_x < 1 || Child_y <1 || Child_x > height || Child_y > width  
                    continue %if child is outside of map or in a negative region, ignore
                end

                if closed_list(Child_x,Child_y) == 1  %check if child node has been checked
                    continue
                end

                dist_x = Child_x-current_nodex; dist_y = Child_y-current_nodey; %determine distance to child node

                if (abs(dist_x) > 1 || abs(dist_y) > 1)
                 Flag = obstacle_jump(dist_x,dist_y,current_node,map); %Check obstacle jumping on current path
                end

               if Flag == 1 %if no objects exist on the desired path
                cost = G(current_nodex,current_nodey) + pdist2(current_node,Child); %child tentative cost
                if open_list(Child_x,Child_y) ==0
                    open_list(Child_x,Child_y) = 1; %add child to open list
                elseif cost >= G(Child_x,Child_y)
                    continue %this is a worse path than before
                end
                parent_X(Child_x,Child_y) = current_nodex; %set parent node to new child
                parent_Y(Child_x,Child_y) = current_nodey;
                G(Child_x,Child_y) = cost; %set child inherent cost
                F(Child_x,Child_y) = cost + H(Child_x,Child_y); %set total cost

               end
            end
        end

        %Reconstruct optimal path if flag is tripped
        
        Optimal(1,:) = [current_nodex current_nodey];
        k = 2;
        while Construct
            %Save temp so current nodes don't get mixed up from parrent
            %array
            current_nodex_dummy = parent_X(current_nodex,current_nodey);
            current_nodey = parent_Y(current_nodex,current_nodey);
            current_nodex = current_nodex_dummy;
            Optimal(k,:) = [current_nodex current_nodey];
            k = k+1;
            if current_nodex == start_x && current_nodey == start_y
                break %Break if we reached parent start
            end
        end

        Optimal = flipud(Optimal); %flip so index 1 is starting point
        optimal_f{w} = Optimal;  %#ok<AGROW> %save all optimal values
        Optimal = []; %Empty Optimal temp so no carry over between points
        %% - test section for the waypoints - %% 
        start_x = End_x; start_y = End_y; %reset the end to the start
        G = zeros(height,width);
        F = single(inf(height,width));
        H = zeros(height,width);
        open_list = zeros(height,width);closed_list = zeros(height,width); %RESET MATRICES
        parent_X = zeros(height,width); parent_Y = zeros(height,width); 
        closed_list(map==1) = 1; %RESET MATRICES
        %  -       END TESTING SECTION      - %
end

end

