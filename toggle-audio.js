const se = new Application('System Events');
// let zoomApp = new Application('Zoom.us');
// zoomApp.activate();

let zoom = se.processes.byName('zoom.us');
if (zoom.exists()) {
	let meetingMenu = zoom.menuBars[0].menuBarItems.byName('Meeting');
	let meetingMenuItems = meetingMenu.menus[0].menuItems;
	for (let i = 0; i < meetingMenuItems.length; i++) {
		let item = meetingMenuItems[i];
		let title = item.title();
		if (item.title() === 'Mute Audio') item.click();
		if (item.title() === 'Unmute Audio') item.click();
	}
}



