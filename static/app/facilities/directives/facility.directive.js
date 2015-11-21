/**
* Post
* @namespace afya360.facilities.directives
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.directives')
    .directive('facility', facility);

  /**
  * @namespace Post
  */
  function facility() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf afya360.facilities.directives.Post
    */
    var directive = {
      restrict: 'E',
      scope: {
        facility: '='
      },
      templateUrl: '/static/templates/facilities/facility.html'
    };

    return directive;
  }
})();