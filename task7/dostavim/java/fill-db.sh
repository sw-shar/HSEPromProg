#!/bin/bash

set -ex

[ $# = 0 ]

# heredoc
mysql dostavim -h db -u root --password=admin <<__EOF__
insert into CLIENT values (1);
insert into LEG values (1, 1, 2, 100, 'train', 10, 20);
insert into ORDERS 
  values (1, '2022-01-01', 1, 1, 2, 'time', 1, 'moving');
insert into PRODUCT values (1, 1, 1, 1);
insert into ROUTE values (1, 1, 1);
insert into ROUTE_LEG values (1, 1, 1, '2022-01-01', '2022-01-02');
__EOF__
