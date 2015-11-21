/**
* Posts
* @namespace afya360.facilities.directives
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.directives')
    .directive('facilities', facilities);

  /**
  * @namespace Posts
  */
  function facilities() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf afya360.facilities.directives.Posts
    */
    var directive = {
      controller: 'PostsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        facilities: '='
      },
      templateUrl: '/static/templates/facilities/facilities.html'
    };

    return directive;
  }
})();