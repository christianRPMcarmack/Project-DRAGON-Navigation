%--------------------------------------------------------------------------

%Project DRAGON Navigation Path Algorithm

%A* GIF plotting function

%Generates animated path of region for viewing/PDR

%Inputs: 
%               -Provided map
%               -Waypoints
%               -Optimal cell array
%               -Desired GIF file name


%Outputs:
%               -None


%Created by Ryan Stewart on 10/11/2018 (separate function created)
%Edited by Ryan Stewart on 10/11/2018

%--------------------------------------------------------------------------


function A_Start_plot(map, waypoints,optimal_f,filename)

%Set figure axis style and interpreter so it looks fancy
set(0,'DefaultFigureColor',[1 1 1]);
set(0,'DefaultLineLineWidth',1.5);
set(0,'DefaultAxesFontSize',24);
set(0,'DefaultTextInterpreter','latex')


hfig = figure; %Call figure and plot the map and the waypoints
imagesc((map))
colormap(flipud(gray)); hold on;
h4 = plot(waypoints(:,2),waypoints(:,1),'b*','MarkerSize',10);

Optimal = cat(1,optimal_f{:});
for i = 1:length(Optimal)
    plot(Optimal(i,2),Optimal(i,1),'r*'); drawnow;hold on;
    frame = getframe(hfig);
    title('Optimal Path using A*');
    xlabel('Y Position'); ylabel('X Position');
    im{i} = frame2im(frame); %#ok<AGROW>
end
    
%Set plot objects for initial, final, and path points for legend
h1 = plot(Optimal(:,2),Optimal(:,1),'r');
h2 = plot(Optimal(1,2),Optimal(1,1),'g*','MarkerSize',10); h3 = plot(Optimal(end,2),Optimal(end,1),'k*','MarkerSize',10);

%basic plotting functionality
grid minor
legend([h1 h2 h3 h4],'Path','Start','End', 'Waypoints');
frame = getframe(hfig);
title('Optimal Path using A*');
xlabel('Y Position'); ylabel('X Position');
im{end+1} = frame2im(frame); 

%write to gif file to save as animation
for idx = 1:length(im)
    [A,map] = rgb2ind(im{idx},256);
    if idx == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',.2);
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',.2);
    end
end
end

