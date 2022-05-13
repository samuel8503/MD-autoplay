# MD-autoplay
* Play Yu-Gi-Oh Master Duel automatically in exhibition event.
## Prerequisites
* Python 3.10.4
* Packages
  * pyautogui >= 0.9.53
  * pillow >= 9.1.0
  * opencv >= 4.5.5.64
## Usage
```bash
python main.py
```
## Limitations
* Your MD application should put under main monitor.
* It's recommanded that your deck should contains only normal monsters.
* Now this can only play under 2560\*1440 resolution (main monitor).
  * If you want to play under other resolutions, the workaround is to replace the screenshots under `target_image` folder.
* How to replace the screenshots under `target_image` folder?
  1. Check out the screenshots under `source_image`, screenshot your own on your monitor.
  2. Clip the corresponding part from screenshots in `source_image`, and put clipped image under `target_image` folder.
    * `battle_pass`'s OK -> `battle_pass`
      * ![image](https://user-images.githubusercontent.com/12276433/168253209-20b8ed19-ac12-4dcc-92a7-932d4985a97b.png)
    * `level_up`'s Get item -> `detect_level_up`
      * ![image](https://user-images.githubusercontent.com/12276433/168253408-4a0c3583-3d60-4498-8aea-efdc20d5c254.png)
    * `loss`'s Profile icon -> `detect_lose`
      * ![image](https://user-images.githubusercontent.com/12276433/168254087-ddfe46af-f207-49e6-9cca-08074f1edd9d.png)
    * `draw`'s Draw -> `draw`
      * ![image](https://user-images.githubusercontent.com/12276433/168253935-44fc4989-a4fb-41fd-bc63-6f8d31429dc5.png)
    * `drop_card`'s Text to tell you to drop one card -> `drop_card`
      * ![image](https://user-images.githubusercontent.com/12276433/168254254-ebf046eb-a7f1-449a-9235-8784432ebbaa.png)
    * `duel`'s DUEL button -> `duel`
      * ![image](https://user-images.githubusercontent.com/12276433/168254376-f1a79a1a-4bcd-4258-938d-39b8287e2ea0.png)
    * `duel_result`'s Back to menu -> `duel_result`
      * ![image](https://user-images.githubusercontent.com/12276433/168254596-1da5bc1a-e26f-4b63-9e15-fcd14b33184d.png)
    * `level_up`'s OK -> `level_up`
      * ![image](https://user-images.githubusercontent.com/12276433/168254702-af537191-37f3-49c3-98d0-e7f713d9aa09.png)
    * `lose`'s OK -> `lose`
      * ![image](https://user-images.githubusercontent.com/12276433/168254804-1181569a-c809-452f-899b-453fee4cf3b7.png)
    * `madel_gain`'s OK -> `madel_gain`
      * ![image](https://user-images.githubusercontent.com/12276433/168254892-1994a17f-536c-4cdd-b0b6-864b50efda71.png)
    * `main1`'s Main 1 -> `main1`
      * ![image](https://user-images.githubusercontent.com/12276433/168254996-61c02dd3-1279-4755-b816-cb5d578114ab.png)
    * `opponent_turn`'s Main -> `opponent_turn`
      * ![image](https://user-images.githubusercontent.com/12276433/168255207-2dd0e4b2-4409-4154-849f-ce8e3fa0eb65.png)
    * `select_phase`'s End phase icon -> `select_phase`
      * ![image](https://user-images.githubusercontent.com/12276433/168255334-96f182d3-1822-45ef-80c5-65c9c3c19063.png)
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
