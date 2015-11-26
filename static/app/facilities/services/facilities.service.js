/**
* Facilities
* @namespace afya360.facilities.services
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.services')
    .factory('Facilities', Facilities);

  Facilities.$inject = ['$http', 'Restangular'];

  /**
  * @namespace Facilities
  * @returns {Factory}
  */
  function Facilities($http, Restangular) {
    Restangular.setBaseUrl('/api/v1');
    Restangular.setDefaultRequestParams('get', {limit: 20});

    Restangular.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
        if (operation === 'getList') {
            var newResponse = data.results;
            return newResponse;
        }
        return data;
    });

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
      // return Restangular.all('health-facilities/').getList({offset:0}).$object;
      return Restangular.all('health-facilities/').getList({offset:0});
    }
  }
})();