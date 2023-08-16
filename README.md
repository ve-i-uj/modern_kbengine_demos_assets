### Логироварие средствами Python

Стандартное логирование Python через модуль `logging` даёт следующие приемущенства: можно задавать формат выходных логов, можно назначать несколько обработчиков логов. Задание формата логов даёт возможность задавать в лог записи место вызова функции логирования, это может быть очень полезно при отладка скриптов KBEngine, т.к. будет точно известно место возникновения лог записи (модуль, номер строки, функцию вызова).

Ниже приведён пример получившихся логов, в которых автоматически встроенной библиотекой указывается строка формирования лог записи и функция вызова (руками набирать точку вызова не нужно!).

<details>
<summary>Пример получившихся логов</summary>

    S_DBG    baseapp01 1000 8001  [2023-08-16 04:39:25 345] - [SpaceAlloc.py:52 - onSpaceCreatedCB()] Spaces::onSpaceCreatedCB: space 1. entityID=0
    S_DBG    baseapp01 1000 8001  [2023-08-16 04:39:25 346] - [Space.py:183 - onGetCell()] Space::onGetCell: 0
    S_DBG    baseapp01 1000 8001  [2023-08-16 04:39:25 346] - [SpaceAlloc.py:65 - onSpaceGetCell()] Spaces::onSpaceGetCell: space 1. entityID=0, spaceKey=7267775145913286656

</details>
<br/>

Модуль `scripts/server_common/assetstools/log.py` не вмешивается в стандарный вывод логов для KBEngine (KBEngine.scriptLogType + вывод на stdout), а построен поверх него. Логи по прежнему работают так, как они работали: с отправкой на Logger компоент. Но теперь есть возможность настраивать их привычными для разработчика на Python средствами.

В модуле `scripts/server_common/assetstools/log.py` содержиться процедуры `setup` и `set_module_log_level`. `log.setup` инициализирует логирование стандартными средствами Python (через модуль logging). Процедуру установки логирования через logging нужно вызвать всего один раз при запуске компонента в kbemain.py, когда компонент будет готов (*один раз для каждого компонента*)

<details>
<summary>Подключение и использование стандартного подхода логирования</summary>

![image](https://github.com/ve-i-uj/enki/assets/6612371/594e042c-7ad3-48c8-b670-d88ced776332)
<br/>
Строки `# from KBEDebug import *` и `# logger.info('onBaseAppReady: isBootstrap=%s' % isBootstrap)` больше не нужны, здесь они приводятся, чтобы показать, что сделано им на замену.

И в скриптах затем можно использовать стандартный подход для логирования

```python
import logging

...

logger = logging.getLogger()


class Spaces(BaseSpacesAPI, KBEngine.Entity, GameObject):

    def __init__(self):
        logger.debug('Initializing ...')  # <-- The logging standart way
        KBEngine.Entity.__init__(self)
        GameObject.__init__(self)
...
```

</details>
<br/>

 这是一个KBEngine服务端demos资产库
========

## 开始

请将kbengine_demos_assets整个文件夹放置于服务端引擎根目录中，通常是这样:

![demo_configure](http://kbengine.github.io/assets/img/screenshots/demo_copy_kbengine.jpg)


## 启动服务端

使用固定参数来启动：(参数的意义:http://www.kbengine.org/cn/docs/startup_shutdown.html)

	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令：

	Linux:
		start_server.sh

	Windows:
		start_server.bat


## 关闭服务端

快速杀死服务端进程:

	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令：

	Linux:
		kill_server.sh

	Windows:
		kill_server.bat


	(注意：如果是正式运营环境，应该使用安全的关闭方式，这种方式能够确保数据安全的存档，安全的告诉用户下线等等)

	Linux:
		safe_kill.sh

	Windows:
		safe_kill.bat


## 直接从代码定义实体（不需要def文件）

https://github.com/kbengine/kbengine_demos_assets/tree/py_entity_def


## Дополнения

### Логирование

При генерировании `assetsapi` можно добавить переменную окружения