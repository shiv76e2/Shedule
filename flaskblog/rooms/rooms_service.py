from importlib.resources import Resource
from flaskblog import db
from flaskblog.models import OrganizationsUsersBelonging, Organizations, OrganizationsResourcesOwnership, Resources
from flaskblog.rooms.dtos import ResourceDto

class RoomsService:
    
    
    def search_available_rooms(user_id):
        '''
            与えられたuser_idのユーザーの所属するorganizationの所有するResourceのListを返す。
            何もなかった場合には空のListを返す。
            1. resourcesを所属するorganizationで絞り込み
            2. ResourceDtoを生成。
        '''


        rooms = Resources.query.join(
            OrganizationsResourcesOwnership, Resources.id==OrganizationsResourcesOwnership.resource_id)\
                .join(Organizations, OrganizationsResourcesOwnership.organization_id == Organizations.organization_id)\
                .join(OrganizationsUsersBelonging, Organizations.organization_id == OrganizationsUsersBelonging.organization_id)\
                .filter(OrganizationsUsersBelonging.user_id == user_id)\
                .all()

        return rooms

                