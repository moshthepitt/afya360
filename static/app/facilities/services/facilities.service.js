/**
* Facilities
* @namespace afya360.facilities.services
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.services')
    .factory('Facilities', Facilities);

  Facilities.$inject = ['$http'];

  /**
  * @namespace Facilities
  * @returns {Factory}
  */
  function Facilities($http) {
    var Facilities = {
      all: all,
    };

    return Facilities;

    ////////////////////

    /**
    * @name all
    * @desc Get all Facilities
    * @returns {Promise}
    * @memberOf afya360.facilities.services.Facilities
    */
    function all() {
      return $http.get('/api/v1/health-facilities/?format=json');
    }
  }
})();