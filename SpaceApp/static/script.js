// $(document).ready(function () {
//
// 	$('.star').on('click', function () {
//       $(this).toggleClass('star-checked');
//     });
//
//     $('.ckbox label').on('click', function () {
//       $(this).parents('tr').toggleClass('selected');
//     });
//
//     $('.btn-filter').on('click', function () {
//       var $target = $(this).data('target');
//       if ($target != 'all') {
//         $('.table tr').css('display', 'none');
//         $('.table tr[data-status="' + $target + '"]').fadeIn('slow');
//       } else {
//         $('.table tr').css('display', 'none').fadeIn('slow');
//       }
//     });
//
//  });

Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: 'Vegetables' },
      { id: 1, text: 'Cheese' },
      { id: 2, text: 'Whatever else humans are supposed to eat' }
    ]
  }
})