import "@jxa/global-type";
import { run } from "@jxa/run";

const zoomStatus = () => {
	return run (() => {
		const se = Application('System Events');
		let zoom = se.processes.byName('zoom.us');
		let zoomStatus = {
      running: false,
      meeting: false,
      audio: false,
      video: false,
      sharing: false,
      recording: false,
		};

		if (zoom.exists()) {
      zoomStatus['running'] = true;

      let meetingMenu = zoom.menuBars[0].menuBarItems.byName('Meeting');
      if (meetingMenu.exists()) {
        zoomStatus['meeting'] = true;

        let meetingMenuItems = meetingMenu.menus[0].menuItems;
        for (let i = 0; i < meetingMenuItems.length; i++) {
          let itemTitle = meetingMenuItems[i].title();
          if (itemTitle === 'Mute Audio') zoomStatus['audio'] = true;
          if (itemTitle === 'Stop Video') zoomStatus['video'] = true;
          if (itemTitle === 'Stop Share') zoomStatus['sharing'] = true;
          if (itemTitle === 'Stop Recording') zoomStatus['recording'] = true;
        }
      }
		}
		return zoomStatus;
	});
};

zoomStatus().then((output) => {
	console.log(output);
}).catch(error => {
	console.log(error);
});

