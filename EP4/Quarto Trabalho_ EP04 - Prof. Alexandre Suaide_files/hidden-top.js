/*global jQuery:false */
jQuery(document).ready(function($) {
"use strict";
	
	$('.toggle-link').each(function() {
	  $(this).click(function() {
		var state = 'open'; //assume target is closed & needs opening
		var target = $(this).attr('data-target');
		var targetState = $(this).attr('data-target-state');

		//allows trigger link to say target is open & should be closed
		if (typeof targetState !== 'undefined' && targetState !== false) {
		  state = targetState;
		}

		if (state == 'undefined') {
		  state = 'open';
		}

		$(target).toggleClass('toggle-link-'+ state);
		$(this).toggleClass(state);      
	  });
	});

	// DESATIVADO NO MOMENTO, NAO CONSEGUI FAZER COM QUE SOMENTE O SUBMENU HOVER FOSSE ATIVADO PELO FIND
	//Menu Bootstrap DropDown hover
	// 	$('ul.nav li.dropdown').hover(function () {
	// 		$(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
	// 	}, function () {
	// 		$(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
	// 	});


});


