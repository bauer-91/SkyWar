from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'background1-':
                list_bg = []
                for i in range (1,5):
                    list_bg.append(Background(f'background1-{i}', (0, 0)))
                    list_bg.append(Background(f'background1-{i}', (576, 0)))
                return list_bg